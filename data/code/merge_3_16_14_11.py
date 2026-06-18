from typing import Any

def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Parameters
    ----------
    number : float
        The numerical value to evaluate. Can be an integer or floating-point number.

    Returns
    -------
    bool
        True if the number is greater than 0, False otherwise.

    Examples
    --------
    >>> is_positive(5)
    True
    >>> is_positive(-3.14)
    False
    >>> is_positive(0)
    False
    """
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [1, -2, 0.5, 0, float('inf'), float('-inf')]

    for num in samples:
        result = is_positive(num)
        print(f"is_positive({num}) -> {result}")