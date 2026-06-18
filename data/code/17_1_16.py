def is_even(number: int) -> bool:
    """
    Check if a given integer is even using the modulo operator.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [10, -3, 42, 0, 7]

    for num in test_cases:
        result = is_even(num)
        print(f"Is {num} even? {result}")