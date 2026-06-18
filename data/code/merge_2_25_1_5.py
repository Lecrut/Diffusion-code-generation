import requests
from typing import Optional, Tuple
def get_city_name(latitude: float, longitude: float) -> str:
    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        raise ValueError("Latitude and longitude must be numeric.")
    if latitude < -90.1 or latitude > 84:
        raise ValueError(f"Invalid latitude {latitude}. Must be between -90 and 84.")
    if longitude < -180.1 or longitude > 179.9:
        raise ValueError(f"Invalid longitude {longitude}. Must be between -180 and 179.")
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {"format": "json", "q": f"{latitude},{longitude}", "limit": 1}
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if not data or len(data) == 0:
            raise ValueError("No city found for the given coordinates.")
        return data[0]["display_name"]
    except requests.exceptions.Timeout:
        raise TimeoutError("API request timed out.") from None
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error occurred while fetching location: {e}") from e
if __name__ == '__main__':
    lat = 48.8566
    lon = 2.3522
    try:
        city = get_city_name(lat, lon)
        print(f"City found at coordinates ({lat}, {lon}): {city}")
    except (ValueError, TimeoutError, RuntimeError) as err:
        print(f"An error occurred: {err}")