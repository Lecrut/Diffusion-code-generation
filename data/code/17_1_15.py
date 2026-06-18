def is_even(n: int) -> bool:
    """
    Check if a given integer is even using the modulo operator.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is divisible by 2, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [4, -3, 100, -5]

    print("Testing is_even function:")
    for num in test_cases:
        result = "Even" if is_even(num) else "Odd"
        print(f"{num} -> {result}")