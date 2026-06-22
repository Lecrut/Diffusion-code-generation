def calculate_total_volume(objects):
    VOLUME_THRESHOLD = 0.0
    total_volume = 0.0
    for volume in objects.values():
        if volume < VOLUME_THRESHOLD:
            raise ValueError("Volume cannot be negative.")
        total_volume += volume
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'pyramid': 21.6,
        'torus': 78.54,
        'ellipsoid': 300.0
    }
    print(calculate_total_volume(sample_objects))