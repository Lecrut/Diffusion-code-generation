import math

def is_odd(n: int) -> bool:
    """
    Determine if a given integer is odd.

    This function checks the parity of an integer `n`. If `n` leaves a remainder
    of 1 when divided by 2, it is considered odd; otherwise, it is even.

    Parameters:
        n (int): The number to check for oddness.

    Returns:
        bool: True if the number is odd, False otherwise.

    Examples:
        >>> is_odd(5)
        True
        >>> is_odd(42)
        False
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    test_values = [1, -3, 0, 17, 10]

    print("Running is_odd tests with hard-coded values:")
    for val in test_values:
        result = is_odd(val)
        expected = (val % 2 != 0)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_odd({val}) => {result} | Expected: {expected} [{status}]")