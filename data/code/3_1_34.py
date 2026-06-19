def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.5, 24.1, 22.8, 23.9, 24.0]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)