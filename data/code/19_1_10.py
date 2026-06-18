def is_greater(a: int | float, b: int | float) -> bool:
    """
    Returns True if a is strictly greater than b, otherwise False.
    
    Args:
        a (int | float): The first value to compare.
        b (int | float): The second value to compare.
        
    Returns:
        bool: Result of the comparison a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    assert is_greater(10, 5) is True   # Test case 1: straightforward integers
    assert is_greater(3.5, 2.1) is True  # Test case 2: floats
    assert is_greater(-1, -5) is True     # Test case 3: negative numbers
    assert is_greater(0, 0) is False      # Test case 4: equal values (should be false)
    
    print("All internal tests passed.")