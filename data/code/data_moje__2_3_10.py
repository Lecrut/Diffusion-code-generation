def calculate_total_volume(volumes):
    return sum(volumes.values())

if __name__ == '__main__':
    sample_volumes = {
        'cube': 125.0,
        'sphere': 335.1,
        'cylinder': 200.5
    }
    print(calculate_total_volume(sample_volumes))