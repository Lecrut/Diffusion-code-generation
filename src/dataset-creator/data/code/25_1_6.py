import requests
from typing import Optional
def get_city_name(latitude: float, longitude: float) -> str:
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180 degrees.")
    url = "https://geocoding-api.example.com/reverse"
    params = {
        'lat': latitude,
        'lon': longitude,
        'api_key': 'hardcoded_sample_key'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            city_name = data.get('city', {}).get('name')
            if not city_name or isinstance(city_name, str):
                return city_name
            raise ValueError("Invalid API response format.")
        elif response.status_code >= 500:
            raise TimeoutError(f"Server error occurred. Status code: {response.status_code}")
        else:
            raise Exception(f"API returned unexpected status code: {response.status_code}.")
    except requests.exceptions.Timeout:
        raise TimeoutError("Request timed out after 10 seconds.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Unable to connect to the geocoding service.")
if __name__ == '__main__':
    lat = 48.8566
    lon = 2.3522
    try:
        city = get_city_name(lat, lon)
        print(f"City name for {lat}, {lon}: {city}")
    except (ValueError, TimeoutError, ConnectionError) as e:
        error_msg = str(e).replace('\n', ' ') if isinstance(e, Exception) else str(e)
        print(f"Error occurred while retrieving city information: {error_msg}")