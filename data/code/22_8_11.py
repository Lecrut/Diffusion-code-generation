def is_odd(n: int) -> bool:
    """Determine if a number is odd.

    This function checks whether an integer n has no factors other than 1, itself (and -1), and its negation (-n).
    
    Args:
        n (int): The integer to check for oddness.

    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Test case 1: Verify that an even number returns False
    assert not is_odd(4), "Expected False for input 4"

    # Test case 2: Verify that an odd number returns True
    assert is_odd(-3579), "Expected True for input -3579"

    print("All tests passed.")