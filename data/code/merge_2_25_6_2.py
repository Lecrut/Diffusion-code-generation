import requests
from typing import List, Tuple, Optional
class CoordinateValidator:
    def __init__(self):
        self.geocoding_url = "https://nominatim.openstreetmap.org/search"
    def validate_coordinate(self, lat: float, lon: float) -> bool:
        return -90 <= lat <= 90 and -180 <= lon <= 180
    def detect_swapped_coordinates(self, input_str: str) -> Tuple[float, float]:
        parts = input_str.split(',')
        if len(parts) != 2:
            raise ValueError("Invalid coordinate format")
        try:
            val1 = float(parts[0].strip())
            val2 = float(parts[1].strip())
            if self.validate_coordinate(val1) and not self.validate_coordinate(val2):
                return val2, val1
            elif not self.validate_coordinate(val1) and self.validate_coordinate(val2):
                raise ValueError("Coordinate values out of range")
            else:
                if val1 > 90 and -180 <= val2 <= 180:
                    return val2, val1
            return val1, val2
        except ValueError as e:
            raise e
    def correct_coordinate(self, input_str: str) -> Tuple[float, float]:
        try:
            lat, lon = self.validate_and_parse(input_str)
            if not (self.validate_coordinate(lat) and self.validate_coordinate(lon)):
                corrected_lat, corrected_lon = self.detect_swapped_coordinates(input_str)
                return corrected_lat, corrected_lon
        except Exception:
            raise
    def validate_and_parse(self, input_str: str) -> Tuple[float, float]:
        parts = input_str.split(',')
        try:
            val1 = float(parts[0].strip())
            val2 = float(parts[1].strip())
            if not (-90 <= val1 <= 90 and -180 <= val2 <= 180):
                raise ValueError("Latitude out of range")
        except (ValueError, IndexError) as e:
            try:
                swapped_val1 = float(parts[1].strip())
                swapped_val2 = float(parts[0].strip())
                return self.validate_and_parse(f"{swapped_val1},{swapped_val2}")
            except Exception:
                raise e
def fetch_geocoding_data(coords: List[Tuple[float, float]], api_key: str) -> dict:
    results = {}
    for lat, lon in coords:
        params = {
            'format': 'json',
            'q': f"{lon},{lat}",
            'accept-language': 'en'
        }
        try:
            response = requests.get(geocoding_url, params=params)
            if response.status_code == 200 and len(response.json()) > 0:
                results[(lat, lon)] = {
                    "name": response.json()[0]['display_name'],
                    "country": response.json()[0].get('country', 'Unknown')
                }
        except Exception as e:
            print(f"Error fetching data for ({lat}, {lon}): {e}")
    return results
if __name__ == '__main__':
    validator = CoordinateValidator()
    raw_coords_input = [
        "40.7128,-74.0060",                  
        "-74.0060,40.7128",                   
        "95.0000,-30.0000",                                                
        "45.5555,-120.6666"                   
    ]
    processed_coords = []
    for coord_str in raw_coords_input:
        try:
            lat, lon = validator.correct_coordinate(coord_str)
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                processed_coords.append((lat, lon))
        except Exception as e:
            print(f"Error processing {coord_str}: {e}")
    api_key = "YOUR_API_KEY_HERE"                                                                                                                 
    results = fetch_geocoding_data(processed_coords, api_key)
    print("Geocoding Results:")
    for coord in processed_coords:
        name = results.get(coord, {}).get('name', 'No data found')
        country = results.get(coord, {}).get('country', 'Unknown Country')
        print(f"Coordinates {coord}: Name={name}, Country={country}")