from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=41b5120a764fd57b1e36ee91690b985a'

    city = 'Pune'

    city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather) #checking the output
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'humidity':city_weather['main']['humidity'],
        
    }
    return render(request, 'index.html', {'weather' : weather}) #returns the index.html template
