def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The temperature list cannot be empty")
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [23.5, 18.2, 30.0, 25.6, 22.4]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)