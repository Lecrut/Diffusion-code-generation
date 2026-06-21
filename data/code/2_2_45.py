def calculate_total_volume(objects):
    if not isinstance(objects, dict):
        raise ValueError("Input must be a dictionary.")
    return sum(volume for volume in objects.values() if isinstance(volume, (int, float)))

if __name__ == '__main__':
    sample_objects = {
        'pyramid': 30.0,
        'cylinder': 125.66,
        'torus': 78.54
    }
    print(calculate_total_volume(sample_objects))