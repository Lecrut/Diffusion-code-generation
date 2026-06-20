def calculate_total_volume(objects):
    total = 0
    for volume in objects.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_objects = {'cube': 125.0, 'sphere': 33.5, 'cylinder': 50.25}
    result = calculate_total_volume(sample_objects)
    print(result)