def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [72.5, 68.3, 75.0, 71.9, 69.8]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)