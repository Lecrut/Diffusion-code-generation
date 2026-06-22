def calculate_total_volume(volumes):
    total_volume = sum(volumes.values())
    return total_volume

if __name__ == '__main__':
    sample_volumes = {
        'box': 10.5,
        'cylinder': 20.3,
        'sphere': 15.8
    }
    print(calculate_total_volume(sample_volumes))