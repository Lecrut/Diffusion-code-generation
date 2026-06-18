def is_even(n: int) -> bool:
    """
    Check if an integer is even using the modulo operator.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if 'n' is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_values = [10, -3, 42, 0, 7]

    print("Testing is_even function:")
    for val in test_values:
        result = "Even" if is_even(val) else "Odd"
        print(f"{val} -> {result}")