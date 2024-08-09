import requests
import os
from twilio.rest import Client

api_key = "yourapi"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "yoursid"
auth_token = "yourauth"
client = Client(account_sid, auth_token)

parameters = {
    "lat": "48.218725",
    "lon": "125.540771",
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=parameters)
print(response.status_code)
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
if int(condition_code) < 700:
    will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's  going  to rain today, Remember to bring umbrella",
        from_="+18108155648",
        to="+16232854463",
    )
    print(message.status)
