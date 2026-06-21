def calculate_total_volume(objects):
    if not isinstance(objects, dict):
        raise ValueError("Input must be a dictionary.")
    
    total_volume = 0
    for volume in objects.values():
        if not isinstance(volume, (int, float)):
            raise ValueError("All volumes must be numbers.")
        total_volume += volume
    
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'parallelepiped': 120.0,
        'ellipsoid': 350.0,
        'ring': 50.0
    }
    print(calculate_total_volume(sample_objects))