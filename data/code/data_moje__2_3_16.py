def calculate_total_volume(volume_data):
    total = 0
    for volume in volume_data.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {
        'sphere': 10.0,
        'cube': 20.0,
        'cylinder': 30.0
    }
    result = calculate_total_volume(sample_data)
    print(result)