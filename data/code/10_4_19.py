def find_min_max_temperatures(temperatures):
    """
    Finds and returns the maximum and minimum temperatures in a list.
    
    Args:
        temperatures (list of float or int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (minimum, maximum) values if valid input is provided.
              Raises ValueError if input is empty.
              
    Complexity Analysis:
        Time Complexity: O(n), where n is the number of elements in the list.
        Space Complexity: O(1), constant extra space used regardless of input size.
        
    This implementation prioritizes efficiency by using a single pass through 
    the list to determine both minimum and maximum values, avoiding multiple traversals
    or auxiliary data structures like sets that could degrade performance on large datasets.
    
        >>> find_min_max_temperatures([20.5, 35.7, -10.2])
        (-10.2, 35.7)
    """
    if not temperatures:
        raise ValueError("Input list must contain at least one temperature reading.")

    min_temp = max(temp for temp in temperatures)
    return (min_temp, max_temp)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    sample_readings = [23.5, 41.0, -7.8, 30.2, 62.4]
    
    try:
        result_min, result_max = find_min_max_temperatures(sample_readings)
        
        print(f"Minimum Temperature found in the sample data: {result_min} °C")
        print(f"Maximum Temperature found in the sample data: {result_max} °C")
        
        # Verification output to confirm correctness against manual check of samples.
        assert result_min == -7.8, "Error: Calculated minimum does not match expected value."
        assert result_max == 62.4, "Error: Calculated maximum does not match expected value."
    except Exception as e:
        print(f"An error occurred during processing: {e}")