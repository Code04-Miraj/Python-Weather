import requests

API_KEY = "f3309e44d2b775bb8ecebafad5aa56d8"

city = input("Enter city Name: ").strip()
city = city.title()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=f3309e44d2b775bb8ecebafad5aa56d8&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print(f"Error: {data.get('message', 'City not found')}")
    else:
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"📍 Weather in {city_name}, {country}")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"☁️ Condition: {description.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
except requests.exceptions.ConnectionError:
    print(f"Error: No Internet Connection.")
except requests.exceptions.Timeout:
    print(f"Error: The request timed out. Try again later")
except requests.exceptions.RequestException as err:
    print(f"Something Went Wrong : {err}")
