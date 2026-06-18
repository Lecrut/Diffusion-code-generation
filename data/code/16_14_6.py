from typing import Number

def is_positive(value: Number) -> bool:
    """
    Determines if a given numerical value is strictly positive.

    Args:
        value (Number): A number to check against zero.

    Returns:
        bool: True if the number is greater than 0, False otherwise.
    
    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-3)
        False
        >>> is_positive(0)
        False
    """
    return value > 0

if __name__ == '__main__':
    test_values = [1, -2, 0.5, float('inf'), float('-inf')]

    for num in test_values:
        result = is_positive(num)
        print(f"is_positive({num}) = {result}")