import requests
from plyer import notification
from time import sleep

api_key = '6woHIkoawKqFaMgtoi9nXwavJE2pdAL6'

while True:
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()

        user_coordinates = data.get('loc')
        if not user_coordinates:
            print("Coordinates not found in the response.")
            continue

        url = f'https://api.tomorrow.io/v4/weather/forecast?location={user_coordinates}&apikey={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            
            timeline = weather_data.get('timelines', {}).get('minutely', [])
            if timeline:
                minutely_data = timeline[0].get('values', {})
                if minutely_data:
                    temperature = minutely_data.get('temperature')
                    humidity = minutely_data.get('humidity')
                    wind_speed = minutely_data.get('windSpeed')
                    visibility = minutely_data.get('visibility')

                    final_string = (
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s\n"
                        f"Visibility: {visibility} km"
                    )

                    notification.notify(
                        title='Weather Update',
                        message=final_string,
                        # app_icon = "weather.ico",
                        timeout=10
                    )

        sleep(7200)

    except Exception as e:
        sleep(7200)