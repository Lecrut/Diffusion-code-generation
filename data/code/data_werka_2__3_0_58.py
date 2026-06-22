def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [20.0, 21.5, 19.8, 20.4, 22.6]
    try:
        average_temperature = calculate_average_temperature(sample_temperatures)
        print(average_temperature)
    except ValueError as e:
        print(e)