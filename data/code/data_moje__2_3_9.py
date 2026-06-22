def calculate_total_volume(measurements):
    total = 0
    for volume in measurements.values():
        total += volume
    return total

if __name__ == '__main__':
    sample_data = {"sphere": 10.5, "cube": 24.0, "cylinder": 15.5}
    result = calculate_total_volume(sample_data)
    print(result)