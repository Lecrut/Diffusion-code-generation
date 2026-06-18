def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        number (float): The numerical value to check. Can be an integer or float.

    Returns:
        bool: True if the number is greater than 0, False otherwise.
    
    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-3.14)
        False
        >>> is_positive(0)
        False
    """
    return number > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [5, -10, 0, 2.718, float('-inf'), float('inf')]

    for sample in samples:
        result = is_positive(sample)
        print(f"is_positive({sample}) = {result}")