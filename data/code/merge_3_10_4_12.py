def find_extremes(temperatures):
    """
    Finds and returns the maximum and minimum temperatures in a list.
    
    Args:
        temperatures (list of float or int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (max_temp, min_temp).
            
    Raises:
        ValueError: If the input list is empty.
    """
    if not temperatures:
        raise ValueError("Input list cannot be empty.")

    max_temp = float('-inf')
    min_temp = float('inf')

    for temp in temperatures:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
            
    return (max_temp, min_temp)

if __name__ == '__main__':
    # Hard-coded sample values
    sample_readings = [23.5, 19.8, 27.2, 15.4, 23.5, -2.0]

    max_val, min_val = find_extremes(sample_readings)

    print(f"Maximum temperature: {max_val}")
    print(f"Minimum temperature: {min_val}")