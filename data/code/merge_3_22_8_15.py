def is_odd(n: int) -> bool:
    """
    Determine if a given integer is odd.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Test case 1: Known even number should return False
    assert not is_odd(4), "Expected false for input 4"

    # Test case 2: Known odd number should return True
    assert is_odd(5), "Expected true for input 5"

    print("All tests passed successfully.")