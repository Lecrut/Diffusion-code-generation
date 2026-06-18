def compare_large_integers(a: int, b: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type handles arbitrarily large numbers automatically,
    so direct comparison is safe and efficient for this purpose. This function
    encapsulates the logic to return a clear string representation of the result.

    Args:
        a (int): First integer value.
        b (int): Second integer value.

    Returns:
        str: 'a_is_greater', 'b_is_greater', or 'equal'.
    """
    if a > b:
        return "a_is_greater"
    elif b > a:
        return "b_is_greater"
    else:
        return "equal"

if __name__ == '__main__':
    pass
