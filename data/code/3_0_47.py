def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")
    
    total_sum = sum(temperatures)
    count = len(temperatures)
    
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_temperatures = [20.5, 21.2, 19.8, 20.4, 21.6]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)