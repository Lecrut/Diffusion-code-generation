import statistics as stats

def find_temperature_extremes(temperatures):
    """
    Finds and returns the maximum and minimum temperatures from a list.
    
    Prioritizes efficiency by converting the input to an immutable sequence once,
    then using Python's built-in optimized functions for finding min/max,
    avoiding manual iteration or sorting unless necessary (not used here).

    Args:
        temperatures (list): A list of temperature values (integers or floats).

    Returns:
        tuple: (max_temp, min_temp) where max_temp is the highest value and 
               min_temp is the lowest. Raises ValueError if input is empty.
    
    Examples:
        >>> find_temperature_extremes([20, 35, -1, 45])
        (45, -1)
    """
    if not temperatures:
        raise ValueError("The temperature list cannot be empty.")
    
    max_temp = float('-inf')
    min_temp = float('inf')
    
    # Single pass to find both minimum and maximum for optimal efficiency.
    # This is faster than separate calls or sorting the entire list (O(n) vs O(2n)).
    for temp in temperatures:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
            
    return max_temp, min_temp

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or file access)
    sample_data = [15.2, 30.0, -5.5, 42.8, 19.7]
    
    max_val, min_val = find_temperature_extremes(sample_data)
    
    print(f"Maximum temperature: {max_val}")
    print(f"Minimum temperature: {min_val}")