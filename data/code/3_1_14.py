def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings (floats).
    
    Args:
        temperatures (list[float]): List of float values representing temperature readings.
        
    Returns:
        float: The average temperature if the list is non-empty, otherwise None.
    """
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    # Hard-coded sample temperatures for testing purposes.
    sample_temperatures = [23.5, 19.8, 24.0, 26.7, 22.3]
    
    average_temp = calculate_average_temperature(sample_temperatures)
    
    if average_temp is not None:
        print(f"The average temperature is {average_temp}")
    else:
        print("No data provided to calculate the average.")