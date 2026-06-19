def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.4, 25.6, 19.8, 22.0, 24.5]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)