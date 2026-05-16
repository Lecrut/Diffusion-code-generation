def calculate_total_volume(volume_data):
    total_volume = 0
    for volume in volume_data.values():
        total_volume += volume
    return total_volume
if __name__ == '__main__':
    sample_data = {
        "cube": 10.0,
        "sphere": 5.5,
        "cylinder": 12.3,
        "pyramid": 8.8
    }
    total = calculate_total_volume(sample_data)
    print(total)