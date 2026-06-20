def calculate_total_volume(volume_dict):
    total = 0
    for volume in volume_dict.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {
        'cube': 8.0,
        'sphere': 4.18,
        'cylinder': 10.5
    }
    result = calculate_total_volume(sample_data)
    print(result)