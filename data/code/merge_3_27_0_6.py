def check_difference(a: float, b: float) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    This function uses direct comparison which is highly optimized in Python's C implementation.
    For floating-point numbers, this checks for exact equality as per IEEE 754 standards unless 
    specific tolerance requirements were provided (which are not requested here).
    
    Args:
        a: First numerical input.
        b: Second numerical input.
        
    Returns:
        A boolean indicating whether the two inputs are different.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user interaction or external dependencies
    result1 = check_difference(5, 6)
    assert result1 is True
    
    result2 = check_difference(3.0, 3.0)
    assert result2 is False
    
    print(f"Difference between {5} and {6}: {result1}")
    print(f"Equality of {3.0} and {3.0}: not different -> {not result2}")