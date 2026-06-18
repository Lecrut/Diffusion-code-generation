def check_match(value1: object, value2: object) -> bool:
    """
    Returns True if value1 is exactly equal to value2, otherwise False.

    Args:
        value1 (object): The first value to compare.
        value2 (object): The second value to compare.

    Returns:
        bool: True if values are identical, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases
    samples = [
        (42, 42),           # integers
        ("hello", "world"), # strings - expected: False
        ([1, 2], [1, 2]),   # lists - expected: True
        ({'a': 1}, {'b': 1}),# dicts - expected: False
    ]

    for v1, v2 in samples:
        result = check_match(v1, v2)
        print(f"check_match({v1!r}, {v2!r}) -> {result}")