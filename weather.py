# importing modules
import datetime as dt
import requests
import json

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = input("Please Enter City:\n")

# Your API key
API_KEY = "c2e250c0477f3a47bdc37092969e33b9"

# updating the URL
URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

# Sending HTTP request
response = requests.get(URL)


# checking the status code of the request
if response.status_code == 200:

    # retrieving data in the json format
    data = response.json()

    # kelvin to Celsius variable
    KtoC = -272.15

    # take the main dict block
    main = data['main']

    # getting temperature
    temperature = main['temp']
    temperature = temperature * KtoC

    # getting feel like
    temp_feel_like = main['feels_like']
    temp_feel_like = temp_feel_like * KtoC

    # getting the humidity
    humidity = main['humidity']

    # weather report
    weather_report = data['weather']

    # wind report
    wind_report = data['wind']

    print(f"{CITY:-^35}")
    print(f"Temperature: {temperature} degree celsius")
    print(f"Feel Like: {temp_feel_like} degree celcius")
    print(f"Humidity: {humidity}")
    print(f"Weather Report: {weather_report[0]['description']}")
    print(f"Wind Speed: {wind_report['speed']}")
else:
    # showing the error message
    print("Error in the HTTP request")

