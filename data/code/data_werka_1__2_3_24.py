def calculate_total_volume(objects):
    total_volume = sum(objects.values())
    return total_volume

if __name__ == '__main__':
    sample_objects = {
        'box': 10.0,
        'cylinder': 20.5,
        'sphere': 30.75
    }
    total_volume = calculate_total_volume(sample_objects)
    print(total_volume)