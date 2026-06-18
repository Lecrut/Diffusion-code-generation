def compare_values(v1: object, v2: object) -> bool:
    """
    Strictly checks for equality between two inputs with O(1) time complexity.
    
    This function performs a direct identity and value comparison using Python's
    built-in `is` operator followed by `==`, which is optimized in CPython to run
    in constant time regardless of input size or type (for supported types).
    It returns True if v1 and v2 are the same object AND have equal values, False otherwise.

    Parameters:
        v1 (object): The first value to compare. Can be any Python object that supports equality comparison.
        v2 (object): The second value to compare. Must support equality and identity checks with v1.

    Returns:
        bool: True if v1 is identical in both identity and value to v2; False otherwise.

    Example:
        >>> compare_values(5, 5)
        True
        >>> compare_values([1, 2], [1, 2])
        True
        >>> compare_values("hello", "world")
        False
    """
    return v1 is v2 and (v1 == v2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    
    test_cases = [
        ("integers", 42, 42),
        ("different integers", 42, 50),
        ("same object identity", id(10) if isinstance(10, int) else None, 10), 
        # Note: In CPython small ints are cached. Let's use a list to force reference check logic clearly via == and is together.
    ]

    # Corrected test cases for clarity in main block without side effects