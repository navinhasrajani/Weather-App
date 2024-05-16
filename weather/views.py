from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=05e3e68944ef640c36d4dd2413e1264a&units=metric'
    # city="Ahmedabad"

    if request.method=="POST":
        form=CityForm(request.POST)
        form.save()
    
    form  = CityForm()


    cities=City.objects.all()
    weather_data=list()
    for city in cities:
        r=requests.get(url.format(city)).json()
        # print(r.text)

        city_weather={
            'city':city.name,
            'temp': r['main']['temp'],
            "description":r['weather'][0]['description'],
            "icon": r['weather'][0]['icon']
        }
        weather_data.append(city_weather)
    # print(weather_data)
    context={'weather_data':weather_data, 'form':form}
    return render(request,"weather/weather.html",context)

def deleteCity(request,city):
    City.objects.get(name=city).delete()
    return redirect('home')

