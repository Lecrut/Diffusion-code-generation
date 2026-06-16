import numpy as np
def bulk_coordinate_to_name(coordinates):
    code_map = {
        'A': {'lat': 40.7128, 'lon': -74.0060},
        'B': {'lat': 34.0522, 'lon': -118.2437},
    }
    result = []
    if len(coordinates) > 1:
        lats = np.array([c['lat'] for c in coordinates])
        lons = np.array([c['lon'] for c in coordinates])
        matched_indices = []
        unmatched_coords = []
        for idx, coord in enumerate(coordinates):
            if any(abs(coord['lat'] - code_map[k]['lat']) < 0.1 and abs(coord['lon'] - code_map[k]['lon']) < 0.1 
                   for k in code_map.keys()):
                matched_indices.append(idx)
        if len(matched_indices):
            result = [f"{coordinates[i]}'s Name" for i in range(len(coordinates))]
    else:
        name_map = {
            'A': "New York",
            'B': "Los Angeles",
        }
        if coordinates[0] in name_map.values():
            result.append(name_map.get(coordinates[0], f"Unknown: {coordinates}"))
    return result
if __name__ == '__main__':
    sample_coords = [
        {'lat': 40.7128, 'lon': -74.0060},
        {'lat': 35.0, 'lon': -90.0},
        {'lat': 34.0522, 'lon': -118.2437}
    ]
    output = bulk_coordinate_to_name(sample_coords)
    print(output)