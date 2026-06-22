def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.5, 18.2, 30.1, 25.6, 21.4]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)