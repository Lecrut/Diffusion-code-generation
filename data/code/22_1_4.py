def is_odd(number: int) -> bool:
    """
    Checks if a given integer is odd using the modulo operator.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 == 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_values = [0, -5, 3, 42, -7]

    print("Testing is_odd function:\n")
    for val in test_values:
        result = is_odd(val)
        status = "Odd" if result else "Even"
        print(f"{val}: {status}")