def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.
    
    Returns:
        bool: True if a is strictly greater than b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases running without user input
    assert is_greater(10, 5) is True
    assert is_greater(3.14, 2.71) is True
    assert is_greater(-1, -5) is True
    assert is_greater(0, 0) is False
    assert is_greater('a', 'b') is False  # Strings are not numbers but Python allows comparison; logic holds for types if needed