#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:52:49 2018

@author: lechuza
"""
import requests

api_url='http://chainradar.com/api/v1/' #won't work
api_2='http://chainradar.com/api/v1/mro/status/'
payload={'type':'GET'}
payload2={'type':'GET','coin':'mro'} #won't work

response=requests.get(api_2,params=payload)
response=requests.get(api_url,params=payload2)

print(response.json())

#get stats on blocks in a height range
api3='http://chainradar.com/api/v1/bcn/blocks/range/'
payload3={'type':'GET','from':1542700,'to':1542706}
response2=requests.get(api3,params=payload3)

json2=response2.json()

api4='http://chainradar.com/api/v1/mro/blocks/range/1542700/1542706/full'
response3=requests.get(api4,params=payload)
lista_json=response3.json()
len(lista_json[6])

#each json element contains three nested elements having the following headers:
lista_json[6].keys()

lista_json[6]['cc'] #coin name only - just a string element
lista_json[6]['blockHeader'] #meta data on the block
len(lista_json[6]['transactions']) # three transactions... each contain the same keys
lista_json[6]['transactions'][0].keys()
lista_json[6]['transactions'][1].keys()
lista_json[6]['transactions'][2].keys()

