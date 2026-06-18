def compare_temperatures(temp1: float | int, temp2: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Args:
        temp1 (float|int): First temperature value.
        temp2 (float|int): Second temperature value.
        
    Returns:
        str: A description of the comparison result.
    """
    if temp1 > temp2:
        return f"{temp1} is higher than {temp2}"
    elif temp2 > temp1:
        return f"{temp2} is lower than {temp1}"
    else:
        return "Both temperatures are equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 36.5
    t_b = 40.2
    
    result = compare_temperatures(t_a, t_b)
    
    print(result)

    # Additional test case with equal temperatures
    t_c = 18.0
    t_d = 18.0
    result_equal = compare_temperatures(t_c, t_d)
    print(f"Comparison of {t_c} and {t_d}: {result_equal}")

    # Test case where first is lower
    t_e = -5.3
    t_f = 2.1
    result_lower = compare_temperatures(t_e, t_f)
    print(f"Comparison of {t_e} and {t_f}: {result_lower}")