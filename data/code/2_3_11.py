def calculate_total_volume(volumes):
    total = 0
    for obj_type, volume in volumes.items():
        total += volume
    return total

if __name__ == '__main__':
    sample_volumes = {
        'box1': 10.5,
        'cylinder1': 20.0,
        'sphere1': 15.25
    }
    result = calculate_total_volume(sample_volumes)
    print(result)