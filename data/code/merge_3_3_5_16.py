def filter_temperatures(temperatures):
    """
    Filters out temperature readings below 0°C from a list of floats.
    
    Args:
        temperatures (list[float]): List of temperature values in Celsius.
        
    Returns:
        list[float]: A new list containing only non-negative temperatures.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data without user input or external dependencies
    raw_readings = [-5, -2, 1, 3.5, 0, 7.8, -10, 4]
    
    filtered_temperatures = filter_temperatures(raw_readings)
    
    print("Original readings:", raw_readings)
    print("Filtered temperatures (>= 0°C):", filtered_temperatures)