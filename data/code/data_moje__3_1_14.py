def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures) if temperatures else 0.0

if __name__ == '__main__':
    sample_readings = [20.5, 22.3, 19.8, 23.1, 21.0]
    result = calculate_average_temperature(sample_readings)
    print(result)