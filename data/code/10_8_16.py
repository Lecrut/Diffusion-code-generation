def compare_temperature(value1: float, value2: float) -> int:
    """
    Compare two temperature values and return an integer result.
    
    Returns 1 if value1 > value2
    Returns -1 if value1 < value2
    Returns 0 if value1 == value2
    
    Args:
        value1 (float): First temperature value
        value2 (float): Second temperature value
        
    Raises:
        ValueError: If inputs are not numeric
    """
    try:
        float(value1)
        float(value2)
    except TypeError:
        raise ValueError("Inputs must be numeric")

    if value1 > value2:
        return 1
    elif value1 < value2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Test case for greater than
    assert compare_temperature(30.5, 25.0) == 1

    # Test case for less than
    assert compare_temperature(-5.0, -8.0) == 1
    
    assert compare_temperature(10.0, 20.0) == -1

    # Test case for equality (using float comparison that allows minor precision differences if needed, 
    # though exact floats are expected here based on task description)
    assert compare_temperature(45.6789, 45.6789) == 0
    
    print("All tests passed successfully.")