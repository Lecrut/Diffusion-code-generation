def calculate_total_volume(objects):
    total_volume = sum(objects.values())
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'cube': 27.0,
        'sphere': 52.36,
        'cylinder': 141.37
    }
    print(calculate_total_volume(sample_objects))