def filter_temperatures(temperatures):
    """
    Filters out temperature readings below freezing (0°C).
    
    Args:
        temperatures (list of float or int): List of temperature values in Celsius.
        
    Returns:
        list: A new list containing only the non-negative temperature values.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing a large list of temperature readings
    raw_readings = [-5, -2.3, 1, 4, -8, 7.5, -0.5, 12, 3.2]

    processed_temperatures = filter_temperatures(raw_readings)

    print("Filtered temperatures (>= 0°C):")
    for temp in processed_temperatures:
        print(temp)