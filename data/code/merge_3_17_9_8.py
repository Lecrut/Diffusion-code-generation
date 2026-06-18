"""Module to check if a given integer is even."""

def is_even(n: int) -> bool:
    """Check if an integer n is even using bitwise AND operator.

    The most pythonic and efficient method in Python checks the least significant bit.
    If (n & 1) evaluates to True, the number is odd; otherwise, it is even.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is even, False otherwise.
    """
    return not (n % 2 == 0 or n & 1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [4, 7, -6, 0, 3]

    print("Testing even number check:")
    for case in test_cases:
        result = is_even(case)
        status = "Even" if result else "Odd"
        print(f"{case}: {status}")