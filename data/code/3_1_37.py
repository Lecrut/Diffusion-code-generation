def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.4, 25.6, 22.1, 28.9, 27.3]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)