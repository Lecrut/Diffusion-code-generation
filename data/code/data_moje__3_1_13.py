def calculate_average_temperature(temperatures):
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.5, 24.1, 22.8, 25.0, 23.9]
    average = calculate_average_temperature(sample_temperatures)
    print(average)