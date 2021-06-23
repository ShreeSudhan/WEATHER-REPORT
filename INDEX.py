import requests
from pprint import pprint

text_file = open("output.txt", "w")


def weather_data(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                       query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
    return res.json()


def print_weather(result, city):
    text_file.write("{}'s temperature: {}°C ".format(
        city, result['main']['temp']))
    text_file.write("Wind speed: {} m/s".format(result['wind']['speed']))
    text_file.write("Description: {}".format(
        result['weather'][0]['description']))
    text_file.write("Weather: {}".format(result['weather'][0]['main']))


def main():
    city = input('Enter the city:')
    # text_file.write()
    try:
        query = 'q='+city
        w_data = weather_data(query)
        print_weather(w_data, city)
        # text_file.write()
        text_file.close()
    except:
        text_file.write('City name not found...')
        text_file.close()


if __name__ == '__main__':
    main()
