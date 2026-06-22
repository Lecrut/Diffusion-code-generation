def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures) if temperatures else 0

if __name__ == '__main__':
    sample_temperatures = [23.5, 25.1, 22.8, 24.0, 23.9]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)