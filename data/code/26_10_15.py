def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    
    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(10, 10)
        False
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input or external dependencies
    sample_cases = [
        (5, 3),      # Expected: True
        (4, 4),      # Expected: False
        (-1.5, -2.0),# Expected: True (negative numbers)
        ("string", "other"),  # This will raise a TypeError as expected for non-numbers
    ]

    print("Running sample tests...")
    
    try:
        result = is_greater(10, 8)
        assert result == True
        
        result2 = is_greater(7.5, 9.5)
        assert result2 == False
        
        # Testing with negative numbers specifically to ensure robustness
        result3 = is_greater(-5, -10)
        assert result3 == True
        
        print("All assertions passed successfully.")
        
    except AssertionError:
        print("An assertion failed!")