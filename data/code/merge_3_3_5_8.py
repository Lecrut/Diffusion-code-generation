def filter_temperatures(temperatures):
    """
    Filters a list of temperature readings to keep only those at or above freezing (0°C).
    
    Args:
        temperatures (list[float]): A list of floating-point numbers representing temperatures.
        
    Returns:
        list[float]: A new list containing only the non-negative temperature values.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample temperature readings including some below freezing (-5, -2) and some above (18.5, 3).
    sample_readings = [-5.0, 18.5, -2.3, 0.0, 3.7, -1.1]
    
    # Process the data using the filter function
    filtered_temperatures = filter_temperatures(sample_readings)
    
    print("Filtered temperatures (>= 0°C):")
    for temp in filtered_temperatures:
        print(temp)