def calculate_total_volume(volumes):
    return sum(volumes.values())

if __name__ == '__main__':
    sample_volumes = {
        'cube': 100.0,
        'sphere': 50.0,
        'cylinder': 75.0
    }
    print(calculate_total_volume(sample_volumes))