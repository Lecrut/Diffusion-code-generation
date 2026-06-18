def compare_temperatures(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values and returns an integer result.
    
    Returns:
        1 if temp_a > temp_b
       -1 if temp_a < temp_b
        0 if temp_a == temp_b
    
    Raises:
        TypeError: If inputs are not numeric (int or float).
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
    # Test case 1: Greater than (25.5 > 20)
    result = compare_temperatures(25.5, 20)
    assert result == 1, f"Expected 1 for greater than, got {result}"

    # Test case 2: Less than (-5 < -3)
    result = compare_temperatures(-5, -3)
    assert result == -1, f"Expected -1 for less than, got {result}"

    # Test case 3: Equality (0.0 == 0.0)
    result = compare_temperatures(0.0, 0.0)
    assert result == 0, f"Expected 0 for equality, got {result}"

    # Test case 4: Integer inputs with difference
    result = compare_temperatures(100, 99)
    assert result == 1, f"Expected 1 for integer greater than, got {result}"

    print("All tests passed successfully.")