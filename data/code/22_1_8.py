def is_odd(n):
    """
    Check if an integer is odd using the modulo operator.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if 'n' is odd, False otherwise.
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_values = [1, -3, 42, 0, -7]

    for num in test_values:
        result = is_odd(num)
        print(f"{num} is {'odd' if result else 'even'}")