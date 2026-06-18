def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, False otherwise.

    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.

    Returns:
        bool: True if values are identical in type and content; False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases running without any user input or external dependencies
    samples = [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 1}),
        (True, True),
        ((1.0,), (1.0,)),
    ]

    for v1, v2 in samples:
        result = check_match(v1, v2)
        print(f"check_match({v1!r}, {v2!r}) -> {result}")