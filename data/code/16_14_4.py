def is_positive(number: float) -> bool:
    """
    Check if a given number is strictly positive (greater than zero).

    Args:
        number (float): The numerical value to evaluate. Can be an integer or floating-point number, 
                       though type hints specify 'float' for generality in numeric contexts. Integers will work as well due to Python's duck typing and conversion behavior in comparisons.

    Returns:
        bool: True if the number is greater than 0; False otherwise (includes zero and negative numbers).

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
    # Sample test cases with hard-coded values running without user input or external dependencies
    sample_values = [5, -3.14, 0, 2e-10, float('inf'), float('-inf')]

    for value in sample_values:
        result = is_positive(value)
        print(f"is_positive({value!r}) = {result}")