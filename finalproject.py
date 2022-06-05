import json
import requests
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "99637a3bb73b336e4d4b636fa3f86271"

def city_name():
    
#user input needed to retrieve city
    city = input(str("Enter the city name:"))
    # if user continues to enter the zipcode of a city or other format besides string it crashes the program and shows a value error
    try:
            int(city)
            
    except:
            pass
    else:
            raise ValueError("input needs to be string form.")
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "99637a3bb73b336e4d4b636fa3f86271"          
    url = f'{base_url}?q={city}&units=imperial&APPID={appid}'

#getting data from the webservice and formatting it with the format function and then displaying the information in a readable format
    response = requests.get(url)

    data = response.json()
    format_data(data)

def format_data(data): # formats the weather data from json to a readable format
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    humid = data['main']['humidity']

    print('Current Temperature : {} degrees fahrenheit'.format(temp))
    print('High Temperature : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {} %'.format(humid))

def main(): # main function that catches the first mistake the user mistakes before crashing program and showing a value error
    while True:
        prompt = input("We only provide service by entering the city name you wish to view the weather.\nType B to begin:")
        if prompt == 'B' or prompt == 'b':
            try:
                city_name()
            except Exception:
                print("Please only enter the name of the intended city you wish to view.")
                city_name()

main()


