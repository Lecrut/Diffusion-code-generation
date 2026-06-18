def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        number (float): The numerical value to check.

    Returns:
        bool: True if number > 0, otherwise False.
    """
    return number > 0

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    print(is_positive(5))      # Expected output: True
    print(is_positive(-3))     # Expected output: False
    print(is_positive(0.0))    # Expected output: False