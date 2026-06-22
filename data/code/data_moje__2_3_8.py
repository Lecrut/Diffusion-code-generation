def calculate_total_volume(volumes):
    total = 0
    for volume in volumes.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {"cube": 8, "sphere": 33.5, "cylinder": 15.7}
    result = calculate_total_volume(sample_data)
    print(result)