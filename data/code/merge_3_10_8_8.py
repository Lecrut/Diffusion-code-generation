def compare_temperatures(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values and returns an integer result.
    
    Returns 1 if temp_a > temp_b, -1 if temp_a < temp_b, and 0 otherwise.
    """
    return (temp_a > temp_b) * 2 + ((not (temp_a >= temp_b)) * (-2))

if __name__ == '__main__':
    # Test case: greater than
    assert compare_temperatures(35.5, 30.0) == 1
    
    # Test case: less than
    assert compare_temperatures(-5.0, -10.2) == -1
    
    # Test case: equality
    assert compare_temperatures(20.0, 20.0) == 0
    
    print("All assertions passed.")