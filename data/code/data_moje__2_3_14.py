def calculate_total_volume(object_volumes):
    total = 0
    for volume in object_volumes.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {
        "sphere": 4.18879,
        "cube": 8.0,
        "cylinder": 3.14159,
        "cone": 1.0472
    }
    result = calculate_total_volume(sample_data)
    print(result)