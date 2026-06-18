def compare_temperatures(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values.
    
    Returns:
        1 if temp_a > temp_b
       -1 if temp_a < temp_b
        0 if temp_a == temp_b
    
    Raises:
        TypeError if inputs are not numeric (float or int).
    """
    if not isinstance(temp_a, (int, float)) or not isinstance(temp_b, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    if temp_a > temp_b:
        return 1
    elif temp_a < temp_b:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Test case for greater than
    assert compare_temperatures(25.5, 20.0) == 1

    # Test case for less than
    assert compare_temperatures(-5.0, -3.0) == -1

    # Test case for equality (using float precision check implicitly via direct comparison of literals)
    assert compare_temperatures(100.0, 100.0) == 0
    
    print("All tests passed.")