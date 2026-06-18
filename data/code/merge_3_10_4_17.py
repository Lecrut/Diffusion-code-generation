def find_extremes(temperatures):
    """
    Finds and returns the maximum and minimum temperatures in a list.
    
    Args:
        temperatures (list[float]): A list of temperature readings.
        
    Returns:
        tuple[float, float]: A tuple containing (maximum_temperature, minimum_temperature).
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")

    max_temp = min(temp for temp in temperatures)
    min_temp = max(temp for temp in temperatures)
    
    return (max_temp, min_temp)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_readings = [23.5, 18.0, 29.7, 15.2, 24.1]

    try:
        max_val, min_val = find_extremes(sample_readings)
        print(f"Maximum temperature: {max_val}")
        print(f"Minimum temperature: {min_val}")
    except ValueError as e:
        print(f"Error: {e}")