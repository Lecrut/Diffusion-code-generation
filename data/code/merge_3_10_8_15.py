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
        raise TypeError("Both temperature values must be numbers.")

    if temp_a > temp_b:
        return 1
    elif temp_a < temp_b:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Test case for greater than (25.5 > 20)
    assert compare_temperatures(25.5, 20) == 1
    
    # Test case for less than (-5 < -10 is False, so this should return -1 because -5 > -10? 
    # Wait: -5 is greater than -10 mathematically. Let's fix the test logic to be clear.
    # We want a value strictly LESS than b. Example: 20 < 30 -> returns -1.
    assert compare_temperatures(20, 30) == -1
    
    # Test case for equality (50.0 == 50.0)
    assert compare_temperatures(50.0, 50.0) == 0

    # Additional edge cases: integers vs floats
    assert compare_temperatures(30, 29) == 1
    
    print("All assertions passed.")