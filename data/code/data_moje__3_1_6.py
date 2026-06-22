def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.5, 24.1, 22.8, 25.3, 24.7, 23.9, 26.0]
    average = calculate_average_temperature(sample_temperatures)
    print(average)