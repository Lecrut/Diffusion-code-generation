def find_temperature_extremes(temperatures):
    """
    Finds and returns the maximum and minimum temperatures from a list.
    
    Args:
        temperatures (list of float or int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (min_temp, max_temp).
            
    Raises:
        ValueError: If the input list is empty.
    """
    if not temperatures:
        raise ValueError("The list of temperatures cannot be empty.")

    min_temp = float('inf')
    max_temp = float('-inf')

    for temp in temperatures:
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
            
    return (min_temp, max_temp)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    sample_readings = [23.5, 18.0, 29.7, -4.2, 23.5]

    min_val, max_val = find_temperature_extremes(sample_readings)

    print(f"Minimum temperature: {min_val}")
    print(f"Maximum temperature: {max_val}")