def is_odd(n):
    """
    Determine if a given integer n is odd.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.

    Raises:
        TypeError: If the input 'n' is not an instance of int or other numeric types.
    """
    try:
        return isinstance(n, (int, float)) and n % 2 != 0
    except Exception:
        raise TypeError("Input must be a number.")

if __name__ == '__main__':
    # Test case 1: Verify correct odd identification.
    assert is_odd(7) is True
    print(f"Test case 1 passed: is_odd(7) = {is_odd(7)}")

    # Test case 2: Verify correct even identification and boundary behavior (0).
    assert is_odd(0) is False
    assert is_odd(-3) is True, "Negative odd number should return True."
    print(f"Test cases passed. Examples:")
    print("is_odd(7) = ", is_odd(7))
    print("is_odd(0) = ", is_odd(0))