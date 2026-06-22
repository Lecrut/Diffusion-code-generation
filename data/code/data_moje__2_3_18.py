def calculate_total_volume(volume_data):
    total = 0
    for obj_type, volume in volume_data.items():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {
        "cube": 8.0,
        "sphere": 4.19,
        "cylinder": 12.5
    }
    result = calculate_total_volume(sample_data)
    print(result)