def calculate_average_temperature(readings):
    if not readings:
        return 0.0
    total = sum(readings)
    count = len(readings)
    return total / count

if __name__ == '__main__':
    sample_temps = [23.5, 24.1, 22.8, 25.0, 23.9]
    result = calculate_average_temperature(sample_temps)
    print(result)