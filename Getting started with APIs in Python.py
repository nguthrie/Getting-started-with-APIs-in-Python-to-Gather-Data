# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:40:11 2020

@author: nicholas

All credit to Nik Piepenbreier from Medium article: 
    Getting started with APIs in Python to Gather Data
    https://towardsdatascience.com/getting-started-with-apis-in-python-to-gather-data-1185796b1ec3

"""

def part_1():
    # learning about the request library for APIs
    # first commit to github
    # part 1: using an open API to find data and the ISS
    

    response = requests.get("http://api.open-notify.org/iss-now.json")
    # print(response.status_code)
    json_response = response.json()
    dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
    
    # calling the response.get object
    longitude = json_response['iss_position']['longitude']
    latitude = json_response['iss_position']['latitude']
    # print('Longitude: ', longitude)
    # print('Latitude:', latitude)



def part_2(): 
    # part 2: using a secure API and key to get weather data
    # using lat and long 

    secret_key = 'f7b54ca589eb85a1365824b8fb9d992c'
    longitude = -99.328213
    latitude = 42.856447
    
    exclude = 'minutely, hourly, daily, alerts, flags'
    
    url = f'https://api.darksky.net/forecast/{secret_key}/{latitude},{longitude}?units=ca&exclude={exclude}'
    
    response = requests.get(url)
    dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
    # print (dictionary)
    
    response_json = response.json()
    current_summary = response_json['currently']['summary']
    current_temperature = response_json['currently']['temperature']
    current_wind_speed = response_json['currently']['windSpeed']
    
    print(f'The current temperature in Toronto, Ontario is {current_temperature} degrees Celsius and the wind speed is {current_wind_speed} km/h.')
    print(f'The current conditions are: {current_summary}.')
    
    
def part_3():
    response = requests.get('https://www.quandl.com/api/v3/datasets/FSE/BDT_X')
    response_json = response.json()
    dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
    # print(dictionary)
    df = pd.DataFrame(response_json['dataset']['data'], columns = response_json['dataset']['column_names'])
    print(df)
    
if __name__== "__main__":
    
    import requests
    import json
    import pandas as pd
    
    # part_1()
    # part_2()
    part_3()


