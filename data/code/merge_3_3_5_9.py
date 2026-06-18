def filter_temperatures(temperatures):
    """
    Filters out temperature readings below freezing (0°C).
    
    Args:
        temperatures (list of float or int): List of temperature values in Celsius.
        
    Returns:
        list: A new list containing only the non-freezing temperatures.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing a large list of temperature readings
    raw_readings = [-5, -2.5, 1, 3.7, -8, 0, 4.2, -10, 6, -3]

    # Process the data using the filter function
    filtered_temps = filter_temperatures(raw_readings)

    # Output the result for verification (does not require user input or files)
    print("Filtered temperature readings:", filtered_temps)