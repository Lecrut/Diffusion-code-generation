def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, otherwise False.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        A boolean indicating whether a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(10, 5) is True
    assert is_greater(3, 7) is False
    assert is_greater("z", "a") is True
    assert is_greater([2, 4], [1, 3]) is True
    
    # Run a few explicit checks for clarity in the main block
    print(f"is_greater(50, 10): {is_greater(50, 10)}")   # Expected: True
    print(f"is_greater('b', 'a'): {is_greater('b', 'a')}") # Expected: True (lexicographical)