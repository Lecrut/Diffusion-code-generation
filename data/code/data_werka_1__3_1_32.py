def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.5, 25.0, 21.8, 22.4, 24.6]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)