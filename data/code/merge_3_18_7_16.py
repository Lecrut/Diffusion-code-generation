def compare_large_integers(a: int, b: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type supports arbitrary precision and handles 
    large numbers automatically, making direct comparison safe from overflow.
    This function returns a string indicating the relationship between 'a' and 'b'.

    Args:
        a (int): First integer to compare.
        b (int): Second integer to compare.

    Returns:
        str: "greater", "less", or "equal" depending on the comparison result.
    """
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"

if __name__ == '__main__':
    pass
