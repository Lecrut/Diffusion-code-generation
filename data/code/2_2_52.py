VOLUME_THRESHOLD = 0

def calculate_total_volume(objects):
    total_volume = 0
    for volume in objects.values():
        if volume < VOLUME_THRESHOLD:
            raise ValueError("Volume cannot be negative.")
        total_volume += volume
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'cube': 27.0,
        'sphere': 52.36,
        'cylinder': 141.37,
        'cone': 12.57,
        'prism': 94.25,
        'ellipsoid': 300.0
    }
    print(calculate_total_volume(sample_objects))