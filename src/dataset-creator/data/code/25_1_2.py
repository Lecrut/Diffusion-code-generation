import requests
from typing import Optional
def get_city_name(latitude: float, longitude: float) -> str:
    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        raise TypeError("Latitude and longitude must be numeric.")
    if latitude < -90 or latitude > 90:
        raise ValueError(f"Invalid latitude {latitude}. Must be between -90 and 90.")
    if longitude < -180 or longitude > 180:
        raise ValueError(f"Invalid longitude {longitude}. Must be between -180 and 180.")
    url = "https://geocoding-api.example.com/v2/reverse?lat={}&lon={}".format(latitude, longitude)
    try:
        response = requests.get(url, timeout=5.0)
        if response.status_code == 429 or response.status_code >= 500:
            raise TimeoutError("API request timed out or service unavailable.")
        data = response.json()
        city_name = data.get('city', {}).get('name')
        if not city_name:
            return "City name not found in database."
        return city_name
    except requests.exceptions.Timeout as e:
        raise TimeoutError(f"API request timed out after 5 seconds.") from e
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError("Unable to connect to the geocoding service.") from e
if __name__ == '__main__':
    lat = 40.7128
    lon = -74.0060
    try:
        result = get_city_name(lat, lon)
        print(f"City Name: {result}")
    except (TypeError, ValueError, TimeoutError, ConnectionError) as error:
        print(f"An error occurred: {error}")