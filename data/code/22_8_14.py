def is_odd(n):
    """
    Determine if a number is odd.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    
    Raises:
        TypeError: If n is not an integer or float that can be converted to int.
    """
    try:
        num = int(n)
        return num % 2 != 0
    except (TypeError, ValueError):
        raise TypeError("Input must be convertible to an integer.")

if __name__ == '__main__':
    # Test case 1: Expected True for odd number
    assert is_odd(7) is True
    
    # Test case 2: Expected False for even number
    assert is_odd(8) is False

    print("All tests passed successfully.")