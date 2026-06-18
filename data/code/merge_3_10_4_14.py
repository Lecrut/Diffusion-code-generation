def find_extremes(temperatures):
    """
    Finds and returns the maximum and minimum temperatures in a list.
    
    Args:
        temperatures (list of float/int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (min_temp, max_temp).
            
    Raises:
        ValueError: If the input list is empty or not provided.
    """
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")

    min_val = float('inf')
    max_val = float('-inf')

    for temp in temperatures:
        if temp < min_val:
            min_val = temp
        elif temp > max_val:
            max_val = temp
            
    return (min_val, max_val)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    sample_readings = [23.5, 18.0, 29.7, -4.2, 23.5]

    min_temp, max_temp = find_extremes(sample_readings)
    
    print(f"Minimum temperature: {min_temp}")
    print(f"Maximum temperature: {max_temp}")