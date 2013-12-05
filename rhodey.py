#!/usr/bin/env python
# -*- mode: python; encoding: utf-8 -*-

# flask libraries
from flask import abort, redirect, url_for

import GeoIP
import urllib2

gi = GeoIP.open("data/GeoLiteCity.dat",GeoIP.GEOIP_STANDARD)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  #example redirect
  return redirect(url_for('helloworld'))

@app.route("/helloworld")
def helloworld():
  return "Hello World!"

@app.route("/ip/<ip>/geo/maxmind.json")
def maxmindgeoip(ip):
  
  gir = gi.record_by_addr(ip)
  print gir
  return '%s' % gir

@app.route("/ip/<ip>/geo/ipinfo.json")
def geoip_ipinfo(ip):
  f = urllib2.urlopen('http://ipinfo.io/%s/json' % (ip))
  return '%s' % f.read()

if __name__ == "__main__":
    app.run()
