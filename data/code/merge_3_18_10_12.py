import numpy as np

def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    This function performs a simple numeric comparison between two arguments,
    supporting both integers and floats (including NumPy scalar types). It avoids
    any overhead by using Python's native operators for the highest performance.

    Parameters
    ----------
    a : number
        The first value to compare. Can be an int or float.
    b : number
        The second value to compare. Can be an int or float.

    Returns
    -------
    bool
        True if `a > b`, False otherwise.

    Examples
    --------
    >>> is_greater(10, 5)
    True
    >>> is_greater(3.5, 7.2)
    False
    
    Notes
    -----
    The function handles normal Python numbers and NumPy scalar types seamlessly.
    It does not perform any type conversion that would alter the values before comparison.

    References
    ----------
    https://numpy.org/doc/stable/reference/generated/numpy.greater.html (inspired)
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure functionality and no external dependencies.
    assert is_greater(10, 5) is True, "Test 1 failed: should be greater"
    assert is_greater(3.9, 4.0) is False, "Test 2 failed: should not be strictly greater float"
    assert is_greater(-1, -2) is True, "Test 3 failed: negative numbers comparison"
    assert is_greater(5, 5) is False, "Test 4 failed: equal values case"

    # Demonstration output (optional for verification without user interaction).
    print(f"is_greater(100, -2): {is_greater(100, -2)}")