import requests
from typing import Optional, Tuple
def get_city_name(lat: float, lon: float) -> str:
    url = "https://geocoding-api.example.com/v1/reverse"
    try:
        response = requests.get(url, params={"lat": lat, "lon": lon}, timeout=5.0)
        if not 200 <= response.status_code < 300:
            raise ValueError(f"API returned status code {response.status_code}")
        data = response.json()
        city_name = data.get("city", {}).get("name")
        if not city_name or isinstance(city_name, str) and len(city_name.strip()) == 0:
            return "Unknown location"
        return city_name
    except requests.exceptions.Timeout:
        raise TimeoutError("API request timed out after 5 seconds.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to connect to the geocoding service.")
    except ValueError as ve:
        if "invalid" in str(ve).lower():
            return f"Invalid input: {str(ve)}"
        else:
            raise
if __name__ == '__main__':
    lat = 40.7128
    lon = -74.0060
    try:
        city = get_city_name(lat, lon)
        print(city)
    except (ValueError, TimeoutError, ConnectionError) as e:
        if isinstance(e, ValueError):
            print(f"Input Error: {e}")
        elif isinstance(e, TimeoutError):
            print("Timeout occurred.")
        else:
            print(f"Connection failed: {e}")