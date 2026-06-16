import requests
from typing import Optional
def get_city_name(latitude: float, longitude: float) -> str:
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90.")
    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "format": "json",
                "lat": latitude,
                "lon": longitude,
                "limit": 1
            },
            timeout=5.0
        )
        response.raise_for_status()
        data = response.json()
        if not data or len(data) == 0:
            return f"City name unknown for coordinates ({latitude}, {longitude})"
        city_name = data[0].get("display_name", "Unknown")
    except requests.exceptions.Timeout:
        raise TimeoutError("API request timed out.")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error occurred while fetching location: {e}")
    return city_name
if __name__ == '__main__':
    lat = 40.7128
    lon = -74.0060
    try:
        result = get_city_name(lat, lon)
        print(f"City name for {lat}, {lon}: {result}")
    except (ValueError, TimeoutError, RuntimeError) as error:
        print(f"An error occurred: {error}")