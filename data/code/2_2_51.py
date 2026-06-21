def calculate_total_volume(objects):
    total_volume = 0
    for volume in objects.values():
        total_volume += volume
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'box': 10.5,
        'sphere': 4.2,
        'cylinder': 7.8,
        'cone': 3.9
    }
    print(calculate_total_volume(sample_objects))