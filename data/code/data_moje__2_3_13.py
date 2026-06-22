def calculate_total_volume(volume_dict):
    total = 0
    for obj_type, vol in volume_dict.items():
        total += vol
    return total

if __name__ == '__main__':
    samples = {
        "cube": 10.0,
        "sphere": 5.5,
        "cylinder": 7.2
    }
    result = calculate_total_volume(samples)
    print(result)