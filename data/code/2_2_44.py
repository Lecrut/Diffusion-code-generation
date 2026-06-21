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
        'hemisphere': 157.08,
        'spherical_cap': 33.51
    }
    print(calculate_total_volume(sample_objects))