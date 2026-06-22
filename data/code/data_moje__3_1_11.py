def calculate_average_temperature(readings):
    if not readings:
        return 0.0
    return sum(readings) / len(readings)

if __name__ == '__main__':
    sample_temps = [20.5, 21.0, 19.8, 22.3, 21.5]
    result = calculate_average_temperature(sample_temps)
    print(result)