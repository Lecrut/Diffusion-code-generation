def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")
    return sum([temp for temp in temperatures]) / len(temperatures)

if __name__ == '__main__':
    sample_temperatures = [20.5, 21.3, 22.7, 23.4, 24.8]
    try:
        average_temperature = calculate_average_temperature(sample_temperatures)
        print(average_temperature)
    except ValueError as e:
        print(e)