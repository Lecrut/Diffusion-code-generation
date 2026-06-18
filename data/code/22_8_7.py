"""Module to determine if a number is odd."""

def is_odd(n: int) -> bool:
    """Return True if n is an odd integer, False otherwise.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Test case 1: Positive even number
    assert not is_odd(4), "Expected False for positive even number"

    # Test case 2: Negative odd number
    assert is_odd(-3), "Expected True for negative odd number"

    print("All test cases passed.")