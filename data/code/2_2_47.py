def validate_objects(objects):
    if not isinstance(objects, dict):
        raise ValueError("Input must be a dictionary.")
    for volume in objects.values():
        if not isinstance(volume, (int, float)):
            raise ValueError("All volumes must be numbers.")

def calculate_total_volume(objects):
    validate_objects(objects)
    total_volume = sum(objects.values())
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'torus': 78.5,
        'pyramid': 43.3,
        'box': 15.2
    }
    print(calculate_total_volume(sample_objects))