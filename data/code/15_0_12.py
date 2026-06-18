def check_match(value1: any, value2: any) -> bool:
    """
    Checks if two values are exactly equal.

    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.

    Returns:
        bool: True if value1 is identical to value2, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (42, 42),          # Should be True
        ("hello", "world"),# Should be False
        ([1, 2], [1, 3]), # Should be False
        ({'a': 1}, {'a': 1}), # Dictionaries are equal if keys/values match (True)
    ]

    for val1, val2 in sample_cases:
        result = check_match(val1, val2)
        print(f"check_match({val1!r}, {val2!r}) = {result}")