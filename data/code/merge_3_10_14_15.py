def absolute_temperature_difference(t1: float, t2: float) -> float:
    """
    Calculate the absolute difference between two temperature values.
    
    Parameters:
        t1 (float): First temperature value.
        t2 (float): Second temperature value.
        
    Returns:
        float: The positive difference between t1 and t2.
    """
    if t1 > t2:
        return t1 - t2
    else:
        return t2 - t1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    temp_a = 75.0
    temp_b = 82.3
    
    result = absolute_temperature_difference(temp_a, temp_b)
    
    print(f"The temperature difference between {temp_a} and {temp_b} is: {result}")