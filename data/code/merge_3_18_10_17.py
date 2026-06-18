"""Module containing utility functions for numerical comparisons."""

def is_greater(a: float | int, b: float | int) -> bool:
    """
    Determine if 'a' is strictly greater than 'b'.

    This function performs a direct comparison between two numerical values.
    It returns True if the first argument is numerically larger than the second,
    and False otherwise (including cases where they are equal).

    Parameters
    ----------
    a : float or int
        The value to compare against 'b'. Should be in the range [-inf, +inf].
    b : float or int
        The value to compare with 'a'. Should be in the range [-inf, +inf].

    Returns
    -------
    bool
        True if a > b; False otherwise.

    Examples
    --------
    >>> is_greater(5, 3)
    True
    >>> is_greater(10, 10)
    False
    >>> is_greater(-2, -5)
    True
    """
    return a > b

if __name__ == "__main__":
    # Sample test cases to verify functionality without external dependencies.
    print(is_greater(10.5, 5))      # Expected: True (float vs int)
    print(is_greater(-3, -6))       # Expected: True (negative numbers)
    print(is_greater(42, 42))       # Expected: False (equality case)
    print(is_greater(float('inf'), float('-inf')))  # Expected: True