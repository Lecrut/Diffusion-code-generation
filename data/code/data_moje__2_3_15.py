def calculate_total_volume(volumes):
    return sum(volumes.values())

if __name__ == '__main__':
    sample_volumes = {
        'cube': 10.0,
        'sphere': 15.5,
        'cylinder': 8.2
    }
    total = calculate_total_volume(sample_volumes)
    print(total)