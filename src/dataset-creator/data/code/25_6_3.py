import requests
from typing import List, Tuple, Optional
def validate_coordinate(lat: float, lon: float) -> bool:
    return -90 <= lat <= 90 and -180 <= lon <= 180
def detect_and_correct_coordinates(coords: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    corrected = []
    for coord in coords:
        if not validate_coordinate(coord[0], coord[1]):
            swapped_coord = (coord[1], coord[0])
            if -90 <= swapped_coord[0] <= 90 and -180 <= swapped_coord[1] <= 180:
                corrected.append(swapped_coord)
            else:
                raise ValueError(f"Invalid coordinate format after potential swap for {coord}")
        else:
            corrected.append(coord)
    return corrected
def fetch_geocoding_data(coords: List[Tuple[float, float]]) -> dict:
    url = "https://geocode.maps.com/search"
    data = {"json": coords}
    response = requests.post(url, json=data, timeout=10)
    if response.status_code == 200 and len(response.json()) > 0:
        return {coord[0]: coord[1] for coord in corrected_coords}
    else:
        raise Exception("Geocoding service returned no results")
if __name__ == '__main__':
    sample_data = [(45.723, -75.689), (75.689, 45.723), (-10.5, -20.5)]
    corrected_coords = detect_and_correct_coordinates(sample_data)
    result_map = {}
    try:
        for lat, lon in corrected_coords:
            geocoding_result = fetch_geocoding_data(corrected_coords)
            if (lat, lon) in geocoding_result:
                name = f"Lat {lat}, Lon {lon}"
                result_map[name] = {"latitude": lat, "longitude": lon}
    except Exception as e:
        print(f"Error during processing: {e}")