import requests
from typing import List, Tuple, Optional
def validate_coordinate(coord: float) -> bool:
    return -90 <= coord <= 90 if isinstance(coord, (int, float)) else False
def correct_coordinates(coords: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    corrected = []
    for lat, lon in coords:
        is_valid_lat = validate_coordinate(lat) and -180 <= lon <= 180
        if not is_valid_lat or (not validate_coordinate(lon) and -90 < lat < 90):
            temp_lat, temp_lon = lat, lon
            corrected.append((temp_lon, temp_lat))
        else:
            corrected.append(coords[-1])
    return corrected
def get_geocoding_data(coordinates: List[Tuple[float, float]]) -> dict:
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"key": "YOUR_API_KEY", "address": ",".join([f"{lat},{lon}" for lat, lon in coordinates])}
    response = requests.get(url, params=params)
    return response.json()
if __name__ == '__main__':
    sample_coords = [(40.7128, -74.0060), (-95.3698, 30.2672)]
    corrected_list = correct_coordinates(sample_coords)
    geocoding_result = get_geocoding_data(corrected_list)