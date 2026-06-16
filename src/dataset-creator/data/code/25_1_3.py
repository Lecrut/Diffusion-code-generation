import requests
from typing import Optional
def get_city_name(latitude: float, longitude: float) -> str:
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90.")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180.")
    url = "https://geocoding-api.example.com/v2/reverse"
    params = {
        'lat': latitude,
        'lon': longitude,
        'format': 'json'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 429 or response.status_code >= 500:
            raise TimeoutError("API request timed out or service unavailable.")
        data = response.json()
        city_name = data.get('city', {}).get('name')
        if not city_name:
            return "City name not found in database."
        return city_name
    except requests.exceptions.Timeout as e:
        raise TimeoutError(f"API request timed out after 10 seconds.") from e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while fetching location data:") from e
if __name__ == '__main__':
    lat = 48.8566
    lon = 2.3522
    try:
        city = get_city_name(lat, lon)
        print(f"Coordinates ({lat}, {lon}) correspond to the city: {city}")
    except (ValueError, TimeoutError, RuntimeError) as error:
        print(f"An error occurred while determining the city name:")