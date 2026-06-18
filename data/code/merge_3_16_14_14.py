def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        number (float): The numerical value to check.

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
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [1, -5, 0, 3.14, float('-inf'), float('inf')]

    print("Testing is_positive function:")
    for value in test_cases:
        result = is_positive(value)
        print(f"is_positive({value}) = {result}")