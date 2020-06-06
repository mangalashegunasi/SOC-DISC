'''
Created on Jun 04, 2020
@author: Mangala Shegunashi
@author: Ankita Jaiswal
@author: Sujata Yadav
'''
import json
import random
from datetime import datetime
import sys
import logging
import time
from beeply import notes
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from random import uniform
from gmplot import gmplot

deviceId = random.randrange(10000)

def newpoint():
    return uniform(-180,180), uniform(-90, 90)

def getTemperatureJSON():
    #current time and date
    now = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    #random temperature
    random.seed()
    temp=int(random.randint(70,104))
    #location Cordinates
    point = newpoint()
    deviceId = random.randrange(10000)
    jsonObj = json.loads(json.dumps({'date': now, 'temperature': temp, 'deviceId': deviceId , 'location': point}))
    if jsonObj['temperature'] > 108:
        print ("COVID ALERT: User Notified for handshake")
        mybeep = notes.beeps()
        mybeep.hear('C',2000)

def get_Geo_Location_Details():
    location={ "type": "Point", "coordinates": [newpoint()] }
    return json.dumps({'deviceId':deviceId,'location':location})

def getTouchDetails():
    # Random number between 0 and 39
    contact = random.randrange(100)
    isTouched = False
    if contact % 2 == 0:
        isTouched = True
    else:
        isTouched = False

    jsonObj = json.loads(json.dumps({'deviceId':deviceId,'contact':isTouched}))    
    if jsonObj['contact'] == True:
        device_ID_Detail_GoogleMaps()
        print ("COVID ALERT: User Notified for touch")
        mybeep = notes.beeps()
        mybeep.hear('C',2000)
    else:
        print("COVID ALERT: User Notified for handshake")

def getTemperature():
    random.seed()
    temp=int(random.randint(70,104))
    if (temp > 108):
        mybeep = notes.beeps()
        mybeep.hear('D',10000)
    return json.dumps({'deviceId':deviceId,'temperature':temp})


def device_ID_Detail_GoogleMaps():
    latitude_list, longitude_list = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])
    hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
    gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
    # Marker
    gmap.circle(hidden_gem_lat, hidden_gem_lon, 1000,'#ECEAE5' )
    gmap.marker(hidden_gem_lat, hidden_gem_lon, '#FF0000')
    gmap.scatter( latitude_list, longitude_list,'#0000FF',size = 80, marker = False)
    # polygon method Draw a polygon with
    # the help of coordinates
    print("COVID ALERT: Please check <map.html> generated on google maps for any details of COVID positive person near your vicinity")
    gmap.draw( ".//map.html" )
    
def return_random_method():
    getTemperatureJSON()
    getTouchDetails()
    getTemperature()

if __name__ == '__main__':
    return_random_method()
