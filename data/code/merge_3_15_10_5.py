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

    # Test with floats (note: float equality can be tricky in edge cases, but this handles direct comparison correctly for exact values)
    assert check_match(3.14, 3.14) is True
    
    # Test with strings
    assert check_match("hello", "world") is False
    assert check_match("", "") is True

    # Test with mixed types that compare equal (e.g., 1 and '1') - Python treats these as different unless explicitly cast, but == returns True if they evaluate the same in a boolean context? Actually no: int vs str are never equal. Let's verify standard behavior
    assert check_match(42, "42") is False

    # Test with None
    assert check_match(None, None) is True
    
    print("All sample tests passed.")