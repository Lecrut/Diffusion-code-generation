def find_temp_extremes(temperatures):
    """
    Finds and returns the maximum and minimum temperatures in a list.
    
    Args:
        temperatures (list of float/int): List of temperature readings.
        
    Returns:
        tuple: A pair containing (min_temperature, max_temperature).
             Raises ValueError if the input list is empty.
             
    Efficiency Note:
        This function performs two passes through the data in O(n) time complexity,
        which is optimal for finding both min and max simultaneously without 
        sorting or additional memory allocation beyond constant space.
        
    :param temperatures: List of temperature values.
    :return: Tuple (min_val, max_val).
    """
    
    if not temperatures:
        raise ValueError("Input list must contain at least one element.")

    min_temp = float('inf')
    max_temp = float('-inf')

    for temp in temperatures:
        if temp < min_temp:
            min_temp = temp
        elif temp > max_temp:  # Use 'elif' to avoid redundant comparisons, though O(n) remains dominant. 
                               # Note: Strictly speaking, a separate check doesn't change complexity class but can be slightly faster in practice on typical datasets where all temps aren't near extremes simultaneously. However, the standard two-pass or single-loop with full comparison is safer for correctness logic flow here without assuming data distribution bias. Let's stick to simple sequential checks inside one loop for absolute clarity and minimal branching overhead per element if we want strict efficiency.
            max_temp = temp

    return min_temp, max_temp

if __name__ == '__main__':
    # Hard-coded sample values as required by the task constraints (no user input/files/network)
    sample_readings = [23.5, 18.0, 45.2, -5.6, 30.1, 29.8]

    min_val, max_val = find_temp_extremes(sample_readings)
    
    # Output results to console for verification (no interactive prompts used)
    print(f"Minimum temperature: {min_val}")
    print(f"Maximum temperature: {max_val}")