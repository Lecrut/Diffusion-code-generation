def calculate_total_volume(objects):
    total_volume = 0
    for volume in objects.values():
        total_volume += volume
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'cube': 10,
        'sphere': 20,
        'cylinder': 30
    }
    print(calculate_total_volume(sample_objects))