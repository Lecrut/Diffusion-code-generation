def absolute_temperature_difference(temp1: float, temp2: float) -> float:
    """
    Calculates the absolute difference between two temperatures.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        float: The positive difference between the two temperatures.
    """
    return abs(temp1 - temp2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 25.0
    t_b = 30.5
    
    result = absolute_temperature_difference(t_a, t_b)
    
    print(f"Temperature A: {t_a}")
    print(f"Temperature B: {t_b}")
    print(f"Difference (absolute): {result}")