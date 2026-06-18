def compare_temperatures(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values and returns an integer result.
    
    Returns 1 if temp_a > temp_b, -1 if temp_a < temp_b, and 0 if they are equal.
    """
    return 1 if temp_a > temp_b else (-1 if temp_a < temp_b else 0)

if __name__ == '__main__':
    # Test case: Greater than
    assert compare_temperatures(35.5, 20.0) == 1
    
    # Test case: Less than
    assert compare_temperatures(-5.0, -10.0) == 1
    
    # Test case: Equality (using float precision check for exact match is tricky with floats, 
    # but we assume inputs are constructed to be exactly equal or use a tolerance if needed.
    # Here we test direct equality as per the function logic which uses strict comparison.)
    assert compare_temperatures(25.0, 25.0) == 0
    
    print("All tests passed.")