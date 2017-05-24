# !/usr/bin/env python
from __future__ import print_function
from functools import wraps
from pprint import pprint
import sys
import requests
import datetime
import json
import influxdb
from influxdb import client as influxdb

db = influxdb.InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='portcount')

portcount = {}
with open(r'portcountlog.csv', 'r') as h:
    for line in h:
        log = line.strip('\r\n').split(',')
        loglist = []
        logentry = {}
        logentry['measurement'] = "portcount"
        logentry['time'] = log[0]
        logentry['fields'] = {}
        logentry['fields']['ports'] = log[1]
        loglist.append(logentry)
        print (loglist)
        db.write_points(loglist)
