def calculate_average_temperature(readings):
    if not readings:
        return 0.0
    total = sum(readings)
    count = len(readings)
    return total / count

if __name__ == '__main__':
    sample_temperatures = [22.5, 24.0, 19.8, 21.3, 23.7]
    result = calculate_average_temperature(sample_temperatures)
    print(result)