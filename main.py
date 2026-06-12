import requests

city = input("Enter city name: ")

api_key = "eedb637d4346c1135d7ba6113cdcacb3"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

print(data)   # Debug

if response.status_code == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Report")
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

else:
    print("Error:", data.get("message"))
