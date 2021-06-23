import requests
#import os
from datetime import datetime

api_key = 'd419fd825158a666fd2b71c3193ba39e'
location = input(" Enter the City Name:- ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#to open in text format
fo=open("C:\\main.txt",'r')      
for x in fo.read():
    y=x.upper()
    fo1=open("C:\\main.txt",'a')
    fo1.write(y)

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data ['main'] ['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("--------------------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current Temperature is: {:.2f} deg C".format(temp_city))
print("Current Weather desc  :",weather_desc)
print("Current Humidity      :",hmdt, '%')
print("Current_wind speed    :",wind_spd , 'kmph')