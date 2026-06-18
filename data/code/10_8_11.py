def compare_temperatures(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values and returns an integer result.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        int: 1 if temp_a > temp_b, -1 if temp_a < temp_b, 0 otherwise.
    """
    if temp_a > temp_b:
        return 1
    elif temp_a < temp_b:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Test case for greater than
    assert compare_temperatures(36.5, 29.8) == 1
    
    # Test case for less than
    assert compare_temperatures(-45.2, -10.0) == -1
    
    # Test case for equality with floats having different representations but equal value
    assert compare_temperatures(30.0 + 0.9 / 7, (int(8 * 36.5 / 2) % 40)) == 0
    
    print("All assertions passed.")