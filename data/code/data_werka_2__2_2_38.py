def calculate_total_volume(objects):
    total_volume = 0
    for volume in objects.values():
        total_volume += volume
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'cube': 27,
        'sphere': 52.36,
        'cylinder': 141.37,
        'cone': 37.68
    }
    print(calculate_total_volume(sample_objects))