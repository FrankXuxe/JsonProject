from plotly import offline
from plotly.graph_objects import Scattergeo, Layout
import json
from typing import Mapping

infile1 = open('US_fires_9_1.json', 'r')
infile2 = open('US_fires_9_14.json', 'r')

firedata1 = json.load(infile1)
firedata2 = json.load(infile2)


bright1, lats1, lons1 = [], [], []
bright2, lats2, lons2 = [], [], []

for fire1 in firedata1:
    if fire1['brightness'] > 450:
        lat = fire1['latitude']
        lon = fire1['longitude']
        bright = fire1['brightness']
        lats1.append(lat)
        lons1.append(lon)
        bright1.append(bright)


#print(bright1[:5])
#print(lats1[:5])
#print(lons1[:5])


#data = [Scattergeo(lon=lons, lat=lats)]

data1 = [{
    'type': 'scattergeo',
    'lon': lons1,
    'lat': lats1,
    'marker': {
        'size': [0.04*m for m in bright1],
        'color':bright1,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout1 = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {'data': data1, 'layout': my_layout1}

offline.plot(fig, filename='usfire91913.html')


for fire2 in firedata2:
    if fire2['brightness'] > 450:
        lat = fire2['latitude']
        lon = fire2['longitude']
        bright = fire2['brightness']
        lats2.append(lat)
        lons2.append(lon)
        bright2.append(bright)

data2 = [{
    'type': 'scattergeo',
    'lon': lons2,
    'lat': lats2,
    'marker': {
        'size': [0.04*m for m in bright2],
        'color':bright2,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout2 = Layout(title="US Fires - 9/14/2020 through 9/30/2020")

fig = {'data': data2, 'layout': my_layout2}

offline.plot(fig, filename='usfire914930.html')

