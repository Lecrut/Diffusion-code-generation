def check_match(value1, value2):
    """
    Returns True if value1 is exactly equal to value2, False otherwise.
    
    Parameters:
        value1 (any): First value to compare.
        value2 (any): Second value to compare.
        
    Returns:
        bool: True if values are identical, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [
        ("apple", "banana"),      # Expected: False
        (42, 42),                 # Expected: True
        ([1, 2], [3, 2]),         # Expected: False
        ({'a': 1}, {'a': 1}),     # Expected: True
    ]

    for val1, val2 in samples:
        result = check_match(val1, val2)
        print(f"check_match({val1!r}, {val2!r}) -> {result}")