def calculate_total_volume(objects):
    total_volume = sum(volumes for volumes in objects.values())
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'cylinder': 150.0,
        'sphere': 300.0,
        'cube': 200.0
    }
    print(calculate_total_volume(sample_objects))