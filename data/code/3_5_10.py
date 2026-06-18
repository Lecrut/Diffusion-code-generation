def filter_temperatures(temperatures):
    """
    Filters out temperature readings below freezing (0°C) from a list of temperatures.
    
    Args:
        temperatures (list[float]): A list of floating-point numbers representing temperatures in Celsius.
        
    Returns:
        list[float]: A new list containing only the non-negative temperature values.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data without user input or external dependencies
    sample_readings = [-5.2, -1.8, 0.0, 3.4, -7.6, 12.9, -0.5]
    
    filtered_results = filter_temperatures(sample_readings)
    
    # Output the result to verify functionality (no printing required by task but good for verification in local run)
    print(filtered_results)