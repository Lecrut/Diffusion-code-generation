def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [20.5, 21.0, 22.3, 23.7, 24.2]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)