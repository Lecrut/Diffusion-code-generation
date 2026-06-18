def is_odd(number: int) -> bool:
    """
    Checks if a given integer is odd using the modulo operator.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1, 2, -3, 0, 100]

    for num in test_cases:
        result = is_odd(num)
        print(f"{num} is odd: {result}")