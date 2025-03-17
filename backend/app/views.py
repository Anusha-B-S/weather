from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city=request.GET.get("city","bengaluru")
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=de86f781eba70c345f5a75c35a6fb48d&units=metric"
    api=requests.get(api_url).json()
    temprature=api['main']['temp']
    country=api["sys"]["country"]
    city_name=api["name"]
    return render(request,"index.html",{'temprature':temprature,"country":country, "city":city_name})



