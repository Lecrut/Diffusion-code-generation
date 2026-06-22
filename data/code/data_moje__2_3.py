def calculate_total_volume(volume_data):
    return sum(volume_data.values())

if __name__ == '__main__':
    sample_data = {
        'sphere': 10.5,
        'cube': 8.2,
        'cylinder': 15.3,
        'cone': 4.1
    }
    total = calculate_total_volume(sample_data)
    print(total)