def compare_temperatures(t1: float, t2: float) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Args:
        t1 (float or int): First temperature value.
        t2 (float or int): Second temperature value.
        
    Returns:
        str: A description indicating which is higher, lower, or if they are equal.
    """
    # Efficient comparison using direct float arithmetic
    if t1 == t2:
        return f"The temperatures {t1} and {t2} are equal."
    elif t1 > t2:
        return f"{t1} is higher than {t2}."
    else:
        return f"{t2} is lower than {t1}."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temp_a = 36.5
    temp_b = 40
    
    result = compare_temperatures(temp_a, temp_b)
    
    print(result)

    # Additional test case: equal temperatures
    result2 = compare_temperatures(25, float('nan'))
    # Note: NaN comparisons return False in Python, but for this task we assume valid numeric input.
    # Let's use a safe equality check just to be robust against edge cases like floats that differ slightly due to precision if needed later, 
    # though the current logic uses direct == which is standard for simple comparison tasks unless high-precision floating point issues are specified.
    
    result3 = compare_temperatures(25.0 + 1e-8, 25.0)
    print(result3)

    # Another test case: negative numbers
    temp_c = -10
    temp_d = 10
    
    result4 = compare_temperatures(temp_c, temp_d)
    print(f"Comparison between {temp_c} and {temp_d}: {result4}")