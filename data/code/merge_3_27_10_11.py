def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different, False otherwise.

    Args:
        a (float): The first numerical value.
        b (float): The second numerical value.

    Returns:
        bool: True if a != b, else False.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files.
    result1 = check_difference(5.0, 3.2)   # Should be True (different floats)
    result2 = check_difference(42, 42)     # Should be False (equal ints/floats)
    
    print(f"check_difference(5.0, 3.2) returned: {result1}")
    print(f"check_difference(42, 42) returned: {result2}")

    assert result1 is True, "Expected different values to return True."
    assert result2 is False, "Expected equal values to return False."
    
    # Additional edge case test with very close floats (should still be distinct if not bit-wise identical)
    float_a = 0.3 + 0.6
    float_b = 0.9
    # Due to floating point representation, these might differ slightly or be equal depending on calculation precision.
    # Here we just test the direct inequality as per standard 'different' logic unless specified otherwise for epsilon comparisons.
    result3 = check_difference(float_a, float_b) 
    print(f"check_difference(0.9, 0.9) returned: {result3}")