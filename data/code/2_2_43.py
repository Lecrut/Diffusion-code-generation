VOLUME_PRECISION = 2

def calculate_total_volume(objects):
    if not isinstance(objects, dict):
        raise ValueError("Input must be a dictionary.")
    
    total_volume = sum(objects.values())
    return round(total_volume, VOLUME_PRECISION)

if __name__ == '__main__':
    sample_objects = {
        'cube': 34.5,
        'sphere': 100.5,
        'cylinder': 200.75
    }
    print(calculate_total_volume(sample_objects))