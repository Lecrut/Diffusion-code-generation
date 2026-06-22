def calculate_total_volume(volumes):
    total = 0.0
    for volume in volumes.values():
        if isinstance(volume, (int, float)):
            total += volume
    return total

if __name__ == '__main__':
    sample_volumes = {
        'sphere': 33.5,
        'cube': 27.0,
        'cylinder': 12.56
    }
    result = calculate_total_volume(sample_volumes)
    print(result)