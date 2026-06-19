def calculate_total_volume(objects):
    total_volume = sum(volumes.values())
    return total_volume

if __name__ == '__main__':
    volumes = {
        'cube': 27,
        'sphere': 52.36,
        'cylinder': 141.37,
        'cone': 47.12
    }
    print(calculate_total_volume(volumes))