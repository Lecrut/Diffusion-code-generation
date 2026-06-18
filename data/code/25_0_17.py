def is_zero(value):
    """
    Check if a given input number is exactly zero.

    Args:
        value (int | float): The numerical value to check.

    Returns:
        bool: True if the value equals 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -1, 1, 0.0, 3.14]

    print("Testing is_zero function:")
    for val in test_values:
        result = is_zero(val)
        status = "Zero" if result else "Not Zero"
        print(f"{val} -> {status}")