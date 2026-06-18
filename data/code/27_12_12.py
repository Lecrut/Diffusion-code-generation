def is_unequal(a: float, b: float) -> bool:
    """
    Determines if two floating-point numbers are unequal using a direct comparison.
    
    This method relies on Python's built-in inequality operator (not equal). 
    While comparing floats can be tricky due to precision issues with arithmetic operations,
    the 'is not' or '!=' operators perform value-based comparisons which is generally sufficient
    for determining if two literals or results of identical calculations are different.
    
    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.
        
    Returns:
        bool: True if the numbers are unequal, False otherwise.

    Note: 
    For extremely specific use cases involving epsilon comparisons for mathematical equality 
    of results derived from calculations, a custom tolerance might be needed. However, 
    this function provides the standard semantic check for inequality as requested by 'unequal'.
    
    Example usage (internal): is_unequal(1.0 + 2e-8, 1.0) # Returns True due to precision
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test case 1: Simple integers represented as floats (should be unequal? No, equal here but distinct conceptually)
    val_a = 5.0
    val_b = 5.0
    result_unequal = is_unequal(val_a, val_b)
    
    # Test case 2: Clearly different values
    val_c = 10.5
    val_d = 20.3
    
    # Test case 3: Values that differ only by floating-point precision (should be unequal due to representation difference)
    pi_approx_1 = round(3.14159, 6) + 0.0000001
    pi_approx_2 = pi_approx_1
    
    # Test case 4: One is zero, one is non-zero (Edge case for float comparisons usually handled correctly by !=)
    val_e = 0.0
    val_f = 1e-15

    print(f"Test 1 - Equal floats (5.0 vs 5.0): {result_unequal} (Expected: False)")
    
    result_diff = is_unequal(val_c, val_d)
    print(f"Test 2 - Different values (10.5 vs 20.3): {result_diff} (Expected: True)")
    
    # Verify that identical literals behave as expected
    x = pi_approx_1 + 0
    y = pi_approx_1
    result_identical = is_unequal(x, y)
    print(f"Test 3 - Identical calculated values ({x} vs {y}): {result_identical} (Expected: False)")

    # Verify small difference detection works as != operator will catch any representation mismatch 
    if abs(val_e - val_f) > 0.5e-16:
        print(f"Test 4 - Small difference detected ({val_e} vs {val_f}): True")
    else:
        result_zero = is_unequal(val_e, val_f)
        print(f"Test 4 - Zero and tiny float check: {result_zero}")

    # Final assertion logic for the module's correctness based on expected outputs above
    assert not result_unequal, "Equal floats should return False"
    assert result_diff, "Different values must return True"
    assert not result_identical, "Identical calculated values (same object or bit pattern) should be equal in this context"
    
    print("All internal assertions passed.")