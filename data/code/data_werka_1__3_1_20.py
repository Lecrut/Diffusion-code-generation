def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.4, 18.9, 30.1, 25.6, 22.3]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)