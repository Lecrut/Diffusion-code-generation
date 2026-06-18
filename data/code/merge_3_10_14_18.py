import abs

def temperature_difference(temp_a: float, temp_b: float) -> float:
    """
    Calculates the absolute difference between two temperatures.
    
    Parameters:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        float: The positive difference between temp_a and temp_b.
    """
    return abs(temp_a - temp_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or network access
    t1 = 25.0
    t2 = -3.5
    
    result = temperature_difference(t1, t2)
    
    print(f"The difference between {t1} and {t2} is: {result}")