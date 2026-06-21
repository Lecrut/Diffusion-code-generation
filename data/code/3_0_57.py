def calculate_average_temperature(temperatures):
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")
    
    total = sum(temperatures)
    count = len(temperatures)
    
    return total / count

if __name__ == '__main__':
    sample_temperatures = [20.3, 21.7, 22.9, 23.4, 24.8]
    average_temperature = calculate_average_temperature(sample_temperatures)
    print(average_temperature)