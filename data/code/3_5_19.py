def filter_temperatures(temperatures):
    """
    Filters out temperature readings below freezing (0°C) from a list.
    
    Args:
        temperatures (list of float or int): List of temperature values in Celsius.
        
    Returns:
        list: A new list containing only the non-negative temperature values.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing daily high temperatures
    raw_readings = [-5, -2, 1, 3, 7, 4.5, 8, -1, 0, 6]
    
    filtered_data = filter_temperatures(raw_readings)
    
    print("Filtered temperature readings (>= 0°C):")
    for temp in filtered_data:
        print(f"{temp}°C")