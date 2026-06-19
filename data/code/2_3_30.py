def calculate_total_volume(objects):
    total_volume = sum(volumes.values())
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'box': 10,
        'sphere': 5,
        'cylinder': 8
    }
    print(calculate_total_volume(sample_objects))