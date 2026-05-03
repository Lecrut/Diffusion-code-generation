def calculate_total_volume(object_volumes):
    total_volume = 0
    for volume in object_volumes.values():
        total_volume += volume
    return total_volume
if __name__ == '__main__':
    object_data = {
        "cube": 10.0,
        "sphere": 5.5,
        "cylinder": 12.3,
        "pyramid": 8.8
    }
    total = calculate_total_volume(object_data)
    print(total)