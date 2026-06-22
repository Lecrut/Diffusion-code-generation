def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")
    total_sum = sum(temperatures)
    count = len(temperatures)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_temperatures = [26.5, 27.0, 28.3, 29.7, 30.2]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)