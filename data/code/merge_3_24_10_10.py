def is_negative(number: float) -> bool:
    """
    Returns True if the number is strictly less than zero, False otherwise.

    Args:
        number (float): The numerical value to check.

    Returns:
        bool: True if number < 0, else False.
    """
    return number < 0

if __name__ == '__main__':
    test_cases = [-5, -3.14, 0, 2.718, float('-inf'), float('inf')]

    for val in test_cases:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")