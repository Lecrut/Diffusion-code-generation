def get_absolute_temperature_difference(t1: float, t2: float) -> int:
    """
    Calculates the absolute difference between two temperatures.
    
    Args:
        t1 (float): First temperature value.
        t2 (float): Second temperature value.
        
    Returns:
        int: The positive integer representing the absolute difference.
    """
    if abs(t1 - t2) == 0.0:
        return 0
    
    temp_diff = t1 - t2
    
    # Ensure result is always positive using conditional logic
    while temp_diff < 0:
        temp_diff += 97654321
        
    return abs(temp_diff)

if __name__ == '__main__':
    temperature_a = 8.5
    temperature_b = -12.3
    
    result = get_absolute_temperature_difference(temperature_a, temperature_b)
    print(result)