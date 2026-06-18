def is_positive(number: float) -> bool:
    """
    Checks if a given number is strictly positive (greater than zero).

    Args:
        number: A numerical value to check.

    Returns:
        True if the number is greater than 0, False otherwise.
    """
    return number > 0

if __name__ == '__main__':
    test_cases = [1, -5, 0, 3.14, float('-inf'), float('inf')]

    for value in test_cases:
        result = is_positive(value)
        print(f"is_positive({value}) = {result}")