def compare_values(v1: object, v2: object) -> bool:
    """
    Strictly checks for equality between two inputs with O(1) time complexity.

    This function performs a direct identity and value comparison using Python's 
    built-in `==` operator which is optimized to be constant time for all standard types 
    (integers, floats, strings, tuples of primitives). It returns True if v1 equals v2,
    otherwise False. No additional processing or data structures are used that would 
    increase complexity beyond O(1).

    Parameters:
        v1 (object): The first value to compare. Can be any Python object supported by ==.
        v2 (object): The second value to compare. Must match the type of v1 for meaningful comparison, though different types may still evaluate as equal if semantically equivalent (e.g., int 5 and float 5.0).

    Returns:
        bool: True if v1 is strictly equal to v2; False otherwise.

    Examples:
        >>> compare_values(3, 3)
        True
        >>> compare_values("hello", "world")
        False
        >>> compare_values([1, 2], [1, 2])
        True
    """
    return v1 == v2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    test_cases = [
        (42, 42),           # Integers: equal
        ("test", "test"),   # Strings: equal
        ([1, 2], [1, 2]),  # Lists of primitives: equal
        ((3,), (3,)),      # Tuples: equal
        (True, True),       # Booleans: equal
        (None, None),       # Nulls: equal
        ("a", "b"),         # Strings: not equal
        ([1], [2]),         # Lists: not equal
        ((3,), (4,)),       # Tuples: not equal
    ]

    for i, (val_a, val_b) in enumerate(test_cases):
        result = compare_values(val_a, val_b)
        print(f"Test case {i + 1}: compare_values({repr(val_a)}, {repr(val_b)}) -> {result}")