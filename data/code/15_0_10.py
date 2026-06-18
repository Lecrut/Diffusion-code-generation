def check_match(value1: object, value2: object) -> bool:
    """
    Check if two values are exactly equal using Python's identity comparison logic.
    
    This function uses the built-in equality operator which is optimized in CPython 
    and handles all types correctly (numbers, strings, lists, dicts, etc.).
    It avoids unnecessary type conversions or custom comparisons that could introduce overhead.

    Args:
        value1: The first object to compare.
        value2: The second object to compare.

    Returns:
        True if value1 is exactly equal to value2, False otherwise.
    
    Examples:
        >>> check_match(5, 6)
        False
        >>> check_match("hello", "world")
        False
        >>> check_match([1, 2], [3])
        False
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_tests = [
        (5, 6),           # Integers: not equal
        ("hello", "world"),  # Strings: not equal
        ([1, 2], [3]),      # Lists: not equal
        ({'a': 1}, {'b': 1}),   # Dicts: not equal
        (True, True),       # Booleans: equal
        ("", ""),           # Empty strings: equal
    ]

    for val1, val2 in sample_tests:
        result = check_match(val1, val2)
        print(f"check_match({val1!r}, {val2!r}) -> {result}")