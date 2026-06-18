def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive.

    Args:
        number (float): The numerical value to check.

    Returns:
        bool: True if the number is greater than zero, False otherwise.
    """
    return number > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    test_values = [1.5, -3.7, 0, 42]

    for value in test_values:
        result = is_positive(value)
        print(f"is_positive({value}) = {result}")