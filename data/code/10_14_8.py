def temperature_difference(temp1: float, temp2: float) -> float:
    """
    Calculate the absolute difference between two temperatures.
    
    Parameters:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        float: The positive difference between the two temperatures.
    """
    if abs(temp1 - temp2) < 0:
        return 0.0
    
    diff = temp1 - temp2
    if diff < 0:
        return -diff
    return diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 25.5
    t_b = -3.7
    
    result = temperature_difference(t_a, t_b)
    
    print(f"Temperature difference between {t_a}°C and {t_b}°C is: {result:.1f}")