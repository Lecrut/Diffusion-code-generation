def calculate_total_volume(volumes):
    return sum(volumes.values())

if __name__ == '__main__':
    sample_volumes = {
        'cube': 27.0,
        'sphere': 36.5,
        'cylinder': 15.2,
        'pyramid': 8.1
    }
    print(calculate_total_volume(sample_volumes))