def are_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal using a direct comparison.
    
    This method uses Python's native equality operator to check inequality.
    While floating-point comparisons can be sensitive due to precision issues,
    the requirement is simply to determine "unequal" status via standard arithmetic operations.
    For exact mathematical values provided as input (as implied by typical use cases 
    where specific sample values are tested), direct comparison is appropriate and efficient.

    Args:
        a (float): First floating-point number.
        b (float): Second floating-point number.

    Returns:
        bool: True if a != b, False otherwise.
    
    Note:
        Floating-point arithmetic can introduce rounding errors in complex calculations. 
        However, for direct comparison of given values without intermediate computation history,
        the standard inequality operator is the most optimized and readable approach available
        in Python's native floating-point implementation (IEEE 754).

    Example:
        >>> are_unequal(1.0, 2.0)
        True
        >>> are_unequal(3.14159, 3.1416)
        True
        >>> are_unequal(5.0, 5.0)
        False
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (1.0, 2.0),       # Expected: True
        (3.14159, 3.1416),   # Expected: True
        (5.0, 5.0),          # Expected: False
        (float('inf'), float('-inf')),    # Expected: True
        (-0.0, 0.0),         # Expected: False (in Python -0.0 == 0.0)
        (1e-7, 2e-8),       # Expected: True
        (float('nan'), float('nan')),     # Note: NaN != NaN is True in IEEE 754
    ]

    print("Testing floating-point inequality function:")
    for i, (val_a, val_b) in enumerate(test_cases):
        result = are_unequal(val_a, val_b)
        expected = "True" if not ((a := val_a) == (b := val_b)) else ("False", "NaN comparison") 
        # Special handling note: NaN != NaN evaluates to True, which is mathematically correct for IEEE 754
        
        print(f"Test Case {i + 1}: are_unequal({val_a}, {val_b}) = {result}")