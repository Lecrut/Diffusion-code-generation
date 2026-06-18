def find_extreme_temperatures(temperatures):
    """
    Finds and returns the maximum and minimum temperatures in a list.
    
    This function prioritizes efficiency by iterating through the list once,
    maintaining current min/max values as it goes, avoiding redundant passes.
    
    Args:
        temperatures (list of float or int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (min_temperature, max_temperature).
              Raises ValueError if input is empty or not a list.
              
    Time Complexity: O(n) where n is the length of the list.
    Space Complexity: O(1) as only constant extra space is used.
    """
    if not isinstance(temperatures, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    
    if len(temperatures) == 0:
        raise ValueError("Temperature list cannot be empty.")

    min_temp = max_temp = None
    
    for temp in temperatures:
        # Handle potential non-numeric inputs gracefully by attempting conversion
        try:
            numeric_val = float(temp)
        except (TypeError, ValueError):
            continue  # Skip invalid entries without raising an error
            
        if min_temp is None or numeric_val < min_temp:
            min_temp = numeric_val
        
        if max_temp is None or numeric_val > max_temp:
            max_temp = numeric_val

    return min_temp, max_temp

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration
    sample_readings = [23.5, 19.8, 45.0, -5.2, 28.7, "invalid", None, 12.3]
    
    result_min, result_max = find_extreme_temperatures(sample_readings)
    
    print(f"Minimum Temperature: {result_min}")
    print(f"Maximum Temperature: {result_max}")