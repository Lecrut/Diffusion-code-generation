def calculate_average_volume(measurements):
    if not measurements:
        return 0.0
    return sum(measurements) / len(measurements)

if __name__ == '__main__':
    sample_data = [10.5, 20.3, 15.7, 30.1, 12.4]
    result = calculate_average_volume(sample_data)
    print(result)