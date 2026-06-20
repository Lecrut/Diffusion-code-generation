def calculate_total_volume(volume_data):
    return sum(volume_data.values())

if __name__ == '__main__':
    sample_volumes = {
        'sphere': 150.5,
        'cube': 200.0,
        'cylinder': 75.25,
        'cone': 50.0
    }
    total = calculate_total_volume(sample_volumes)
    print(total)