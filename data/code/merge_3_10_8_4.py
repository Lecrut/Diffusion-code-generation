def compare_temperatures(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values.
    
    Returns 1 if temp_a > temp_b, -1 if temp_a < temp_b, and 0 otherwise.
    """
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
    assert compare_temperatures(-5.0, -10.5) == -1
    
    # Test case for equality (float precision check: exact values should match)
    assert compare_temperatures(36.627489, 36.627489) == 0

    print("All assertions passed.")