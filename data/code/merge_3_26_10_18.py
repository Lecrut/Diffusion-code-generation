def is_greater(a: float | int, b: float | int) -> bool:
    """
    Checks if numerical value 'a' is strictly greater than 'b'.

    Args:
        a (float | int): The first numerical argument to compare.
        b (float | int): The second numerical argument to compare.

    Returns:
        bool: True if 'a' > 'b', otherwise False.
    
    Examples:
        >>> is_greater(10, 5)
        True
        
        >>> is_greater(3.14, 2.71)
        True
    
        >>> is_greater(-1, -5)
        False

    Note:
        This function handles both integer and floating-point numbers correctly, 
        including edge cases where values might be equal or negative.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 42
    sample_b = 10
    
    result = is_greater(sample_a, sample_b)
    
    if not result:
        print("Sample Error.")