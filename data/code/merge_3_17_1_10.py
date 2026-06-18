def is_even(num: int) -> bool:
    """
    Checks if an integer is even using the modulo operator.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is even, False otherwise.
    """
    return num % 2 == 0

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    sample_values = [42, -3, 17, 0, 100]

    for value in sample_values:
        result = is_even(value)
        print(f"{value} is {'even' if result else 'odd'}")