def find_min_max_temperatures(temperatures):
    """
    Finds and returns the maximum and minimum temperatures from a list.
    
    Args:
        temperatures (list of float or int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (min_temp, max_temp).
              Raises ValueError if input is empty.
              
    Time Complexity: O(n) - Single pass through the list.
    Space Complexity: O(1) - Constant extra space used.
    """
    if not temperatures:
        raise ValueError("Input list cannot be empty.")

    min_temp = max_temp = temperatures[0]

    for temp in temperatures[1:]:
        if temp < min_temp:
            min_temp = temp
        elif temp > max_temp:
            max_temp = temp
            
    return (min_temp, max_temp)

if __name__ == '__main__':
    sample_readings = [23.5, 19.0, 27.8, 15.2, 23.5, -4.6]
    
    min_val, max_val = find_min_max_temperatures(sample_readings)

    print(f"Minimum temperature: {min_val}")
    print(f"Maximum temperature: {max_val}")