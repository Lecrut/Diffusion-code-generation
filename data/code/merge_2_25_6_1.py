import requests
from typing import List, Tuple, Optional
def validate_coordinate(coord: float) -> bool:
    return -90 <= coord <= 90 if "lat" in str(coord).lower() else -180 <= coord <= 180
def correct_coordinates(coords: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    corrected = []
    for lat, lon in coords:
        is_lat_valid = validate_coordinate(lat)
        is_lon_valid = validate_coordinate(lon)
        if not (is_lat_valid and is_lon_valid):
            if abs(lat - 90.5) < abs(lon - 180.5) or abs(lat + 90.5) < abs(lon - (-180.5)):
                corrected.append((lon, lat))
        else:
            corrected.append((lat, lon))
    return corrected
def fetch_geocoding(coords: List[Tuple[float, float]]) -> dict:
    url = "https://api.mapbox.com/geocode/v5/mapbox.geocode"
    headers = {"Authorization": "pk.eyJ1IjoiZXhhbXBsZSIsImEiOiJja2N3eWVqMzQwYmRlMG4yZW80dGh6aDBvIn0.example_token"}
    data = {
        "text": ",".join([f"{c[0]},{c[1]}" for c in coords]),
        "limit": 5,
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json() if response.status_code == 200 else {"error": f"Status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
if __name__ == '__main__':
    sample_coords = [(45.1, -76.3), (-98.5, 20.1), (25.1, 50.0)]
    corrected_list = correct_coordinates(sample_coords)
    geocoding_result = fetch_geocoding(corrected_list)
    print(geocoding_result.get("features", []))