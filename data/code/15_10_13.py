def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, False otherwise.
    
    Args:
        value1: First argument to compare.
        value2: Second argument to compare.
        
    Returns:
        Boolean indicating equality of the two arguments.
    """
    return value1 == value2

if __name__ == '__main__':
    # Hard-coded sample values for testing
    samples = [
        (5, 5),           # Should be True
        ("hello", "world"), # Should be False
        ([1, 2], [1, 2]), # Should be True
        ({'a': 1}, {'b': 1}), # Should be False
    ]

    for val1, val2 in samples:
        result = check_match(val1, val2)
        print(f"check_match({val1!r}, {val2!r}) = {result}")