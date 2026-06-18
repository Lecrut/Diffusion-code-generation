import requests
from typing import Optional
def get_city_name(latitude: float, longitude: float) -> str:
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "format": "json",
            "q": f"{latitude},{longitude}",
            "limit": 1
        }
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data[0].get("display_name", "")
        else:
            raise ValueError(f"API returned status code {response.status_code}")
    except requests.exceptions.Timeout:
        raise TimeoutError("Request timed out")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error occurred: {e}")
if __name__ == '__main__':
    lat = 40.7128
    lon = -74.0060
    try:
        city = get_city_name(lat, lon)
        print(city)
    except TimeoutError as te:
        print(f"Timeout error occurred: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")