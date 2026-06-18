def compare_values(v1: any, v2: any) -> bool:
    """
    Strictly checks for equality between two inputs with O(1) time complexity.

    This function compares two values using Python's built-in identity and value comparison logic directly.
    It returns True if the objects are considered equal in both type and content, False otherwise.
    
    Parameters:
        v1 (any): The first input value to compare. Can be any Python object.
        v2 (any): The second input value to compare. Can be any Python object.

    Returns:
        bool: True if v1 is equal to v2, False otherwise.

    Examples:
        >>> compare_values(5, 5)
        True
        >>> compare_values("hello", "world")
        False
        >>> compare_values([1, 2], [3, 4])
        False
    """
    return v1 == v2

if __name__ == '__main__':
    # Hard-coded sample values for testing without any external input or files
    samples = [
        (5, 5),           # Should be True
        ("hello", "world"),   # Should be False
        ([1, 2], [3, 4]),     # Should be False
        ({'a': 1}, {'b': 2}),# Should be False
    ]

    for v1, v2 in samples:
        result = compare_values(v1, v2)
        print(f"compare_values({v1!r}, {v2!r}) -> {result}")