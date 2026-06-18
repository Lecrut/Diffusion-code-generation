def compare_temperatures(temp1: float | int, temp2: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.

    Args:
        temp1 (float|int): First temperature value.
        temp2 (float|int): Second temperature value.

    Returns:
        str: A message indicating which temperature is higher, lower, or if they are equal.
    """
    # Direct comparison is efficient and sufficient for numeric types in Python 3.x
    if temp1 > temp2:
        return f"{temp1} degrees is hotter than {temp2} degrees."
    elif temp2 > temp1:
        return f"{temp2} degrees is colder than {temp1} degrees."
    else:
        return f"Both temperatures are equal at {temp1} degrees."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 75.0
    t_b = 82
    
    result = compare_temperatures(t_a, t_b)
    print(result)

    # Additional test case where first is lower
    result_2 = compare_temperatures(10, -5)
    print(result_2)

    # Test case for equality
    result_3 = compare_temperatures(-10.5, -10.5)
    print(result_3)