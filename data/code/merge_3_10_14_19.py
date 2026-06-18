def temperature_difference(t1: float, t2: float) -> float:
    """
    Calculates the absolute difference between two temperatures.
    
    Args:
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
    # Hard-coded sample values for testing without user input or network access
    temp_a = 25.0
    temp_b = 30.5
    
    result = temperature_difference(temp_a, temp_b)
    
    print(f"Temperature difference between {temp_a} and {temp_b}: {result}")