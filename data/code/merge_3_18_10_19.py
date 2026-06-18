import numpy as np

def is_greater(a: float | int, b: float | int) -> bool:
    """
    Check if a numerical value 'a' is strictly greater than another value 'b'.

    Parameters
    ----------
    a : number
        The first numerical argument. Can be an integer or floating-point number.
    
    b : number
        The second numerical argument. Can be an integer or floating-point number.

    Returns
    -------
    bool
        True if 'a' is strictly greater than 'b', False otherwise.

    Notes
    -----
    This function performs a direct comparison and returns the result immediately,
    ensuring high efficiency for both integers and floats. It handles standard numeric
    types but does not perform any type conversion or validation beyond basic usage.

    Examples
    --------
    >>> is_greater(5, 3)
    True
    >>> is_greater(2, 7)
    False
    
    References
    ----------
    Python's built-in comparison operators (`>`) are used for optimal performance.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5

    result = is_greater(sample_a, sample_b)
    print(f"is_greater({sample_a}, {sample_b}) = {result}")