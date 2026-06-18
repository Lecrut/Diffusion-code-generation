def is_odd(n: int) -> bool:
    """
    Checks if an integer n is odd using the modulo operator.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n % 2 == 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, -3, 5, 42, -7, 9]

    for num in test_cases:
        result = is_odd(num)
        print(f"is_odd({num}) = {result}")