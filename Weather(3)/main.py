import requests
import json
import pyttsx3
engine = pyttsx3.init()

city = input("Enter the name of the city: \n")

url = f"https://api.weatherapi.com/v1/current.json?key=b17a4020b41e41eba8472905250108&q={city}"

r = requests.get(url)
print(r.text)
wdic =json.loads(r.text)
t = wdic["current"]["temp_c"]
a = wdic["location"]["country"]
b = wdic["current"]["wind_kph"]
h = wdic["current"]["humidity"]
c = wdic["current"]["cloud"]
f = wdic["current"]["feelslike_c"]
condition = wdic["current"]["condition"]["text"]

engine.say(f'The weather in the {city}, {a} is {t} degrees , mostly like {condition} and the wind speed is {b} kilometers per hour.The humidity is {h} with cloud of {c}, feels like {f}')
engine.runAndWait()


