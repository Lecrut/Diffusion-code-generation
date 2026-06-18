import numpy as np

def is_greater(a: float, b: float) -> bool:
    """
    Determine if a strictly greater than b.

    Parameters
    ----------
    a : float or numeric type comparable to float
        The first numerical value to compare against the second argument.
    
    b : float or numeric type comparable to float
        The second numerical value to compare against the first argument.

    Returns
    -------
    bool
        True if a > b, otherwise False.

    Examples
    --------
    >>> is_greater(5.0, 3)
    True
    """
    return a > b

if __name__ == '__main__':
    test_cases = [
        (10, 5),       # Expected: True
        (3.5, 4),      # Expected: False
        (-1, -2),      # Expected: True
        (int(float("inf")), float("-inf")),  # Edge case with infinity
    ]

    for i, args in enumerate(test_cases):
        a, b = args
        result = is_greater(a, b)
        print(f"is_greater({a}, {b}) == {result}")