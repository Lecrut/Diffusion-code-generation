def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, False otherwise.
    
    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.
        
    Returns:
        bool: True if values are identical, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 5),           # Should be True
        ("hello", "world"),   # Should be False
        ([1, 2], [3, 4]),     # Should be False
        ({'a': 1}, {'b': 2}), # Should be False
    ]

    for val1, val2 in test_cases:
        result = check_match(val1, val2)
        print(f"check_match({val1!r}, {val2!r}) = {result}")