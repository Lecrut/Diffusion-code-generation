import requests
from typing import List, Tuple, Optional
def validate_coordinate(coord: float) -> bool:
    return -90 <= coord <= 90 if isinstance(coord, (int, float)) else False
def clean_coordinates(coords: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    cleaned = []
    for lat, lon in coords:
        try:
            lat_val = float(lat)
            lon_val = float(lon)
            if not validate_coordinate(lat_val):
                continue
            if not validate_coordinate(lon_val):
                continue
            swapped_lat = -lon_val
            swapped_lon = lat_val
            if abs(swapped_lat) <= 90 and abs(swapped_lon) <= 180:
                cleaned.append((swapped_lat, swapped_lon))
            else:
                cleaned.append((lat_val, lon_val))
        except (ValueError, TypeError):
            continue
    return cleaned
def geocode_coordinates(coords: List[Tuple[float, float]], api_key: str) -> dict:
    results = []
    for lat, lon in coords:
        url = f"https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            'latlng': f'{lon},{lat}',                                                                                                                                                                                                                                     
            'key': api_key,
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            if status_code := data.get('status') == 'OK':
                results.append({
                    'name': data['results'][0].get('formatted_address', ''),
                    'lat': lat,
                    'lon': lon
                })
        except requests.RequestException:
            continue
    return {'success_count': len(results), 'data': results}
if __name__ == '__main__':
    sample_coords = [
        (40.7128, -74.0060),                 
        (-35.8619, -58.3849),                                    
        (100.0, 100.0),                              
        ('invalid', '20'),                                   
    ]
    api_key = "YOUR_API_KEY_HERE"
    cleaned_data = clean_coordinates(sample_coords)
    print(f"Cleaned coordinates count: {len(cleaned_data)}")
    final_result = geocode_coordinates(cleaned_data, api_key)
    if 'data' in final_result and len(final_result['data']) > 0:
        for item in final_result['data']:
            print(item)