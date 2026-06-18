import requests
from typing import Optional, Tuple
def get_city_name(latitude: float, longitude: float) -> str:
    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        raise TypeError("Latitude and longitude must be numeric values.")
    if latitude < -90 or latitude > 90:
        raise ValueError(f"Invalid latitude {latitude}. Must be between -90 and 90.")
    if longitude < -180 or longitude > 180:
        raise ValueError(f"Invalid longitude {longitude}. Must be between -180 and 180.")
    url = f"https://geocoding-api.example.com/reverse?lat={latitude}&lon={longitude}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("city", "Unknown City")
        else:
            error_msg = f"API returned status code {response.status_code}"
            raise RuntimeError(error_msg)
    except requests.exceptions.Timeout:
        raise TimeoutError(f"Request to geocoding API timed out after 5 seconds.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to connect to the geocoding service.")
if __name__ == '__main__':
    lat = 40.7128
    lon = -74.0060
    try:
        city_name = get_city_name(lat, lon)
        print(f"City Name: {city_name}")
    except (TypeError, ValueError, TimeoutError, ConnectionError) as e:
        print(f"An error occurred: {e}")