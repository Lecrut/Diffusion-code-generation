def calculate_total_volume(volume_dict):
    total = sum(volume_dict.values())
    return total

if __name__ == '__main__':
    sample_volumes = {
        'cube': 8.0,
        'sphere': 36.5,
        'cylinder': 12.3,
        'pyramid': 5.7
    }
    result = calculate_total_volume(sample_volumes)
    print(result)