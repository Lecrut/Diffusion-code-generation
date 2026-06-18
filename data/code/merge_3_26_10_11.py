def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float or int): The first numerical argument to compare.
        b (float or int): The second numerical argument to compare.

    Returns:
        bool: True if a > b, False otherwise.
    
    Example:
        >>> is_greater(5, 3)
        True
        >>> is_greater(10, 10)
        False
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases run without any external input or files.
    samples = [
        (5, 3),      # Should be True
        (4, 4),      # Should be False (equal)
        (-10, -20),  # Should be True
        ("not a number", "another"),  # Will raise TypeError as expected for non-numeric inputs in Python comparison of strings to numbers depending on context but here string vs int/float is not strictly numeric so we assume type hint enforcement. However python allows str > int with lexicographical ordering if mixed? No, actually it raises TypeError. So this is robust only if types are correct per spec "numerical arguments".
    ]

    # Note: The above sample includes strings which will cause a TypeError because the function expects numerical arguments as per docstring and task description ("numerical arguments"). 
    # Adjusting to valid numbers for safety in standalone execution.
    safe_samples = [
        (5, 3),      # True
        (10, 20),     # False
        (-5, -8),     # True
    ]

    print("Testing is_greater function:\n")
    test_count = 0
    pass_count = 0
    
    for val_a, val_b in safe_samples:
        result = is_greater(val_a, val_b)
        expected_result = (val_a > val_b)
        
        if not isinstance(result, bool):
            print(f"ERROR: Non-boolean return value for {val_a} vs {val_b}")
            
        elif result != expected_result:
            print(f"MISMATCH: is_greater({val_a}, {val_b}) returned {result}, expected {expected_result}")
        else:
            pass_count += 1
            
        test_count += 1
    
    if pass_count == test_count:
        print("\nAll tests passed!")
    else:
        print(f"\n{test_count - pass_count} out of {test_count} tests failed.")