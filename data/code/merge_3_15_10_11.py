def check_match(value1: any, value2: any) -> bool:
    """
    Check if two values are exactly equal.

    Args:
        value1: The first value to compare.
        value2: The second value to compare.

    Returns:
        True if value1 is exactly equal to value2, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    
    # Test with integers
    assert check_match(5, 5) is True
    assert check_match(5, 6) is False

    # Test with strings (case-sensitive and whitespace-sensitive)
    assert check_match("hello", "hello") is True
    assert check_match("Hello", "hello") is False
    assert check_match("test ", " test ") is False

    # Test with floats (exact match required, not approximate)
    assert check_match(3.14, 3.14) is True
    assert check_match(3.14, 3.15) is False

    # Test with lists and tuples (structural equality matters)
    assert check_match([1, 2], [1, 2]) is True
    assert check_match((1, 2), [1, 2]) is False  # Different types
    assert check_match([1, 2, 3], [1, 2]) is False

    print("All sample tests passed.")