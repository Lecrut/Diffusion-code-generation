def calculate_total_volume(object_volumes):
    total = 0
    for volume in object_volumes.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {
        "box": 100,
        "sphere": 50,
        "cylinder": 75
    }
    result = calculate_total_volume(sample_data)
    print(result)