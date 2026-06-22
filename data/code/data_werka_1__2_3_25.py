def calculate_total_volume(objects):
    total_volume = sum(volumes for volumes in objects.values())
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'cube': 27,
        'sphere': 52.36,
        'cylinder': 141.37
    }
    total_volume = calculate_total_volume(sample_objects)
    print(total_volume)