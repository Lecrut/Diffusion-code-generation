def is_odd(n: int) -> bool:
    """
    Determine if a given integer is odd.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    
    Raises:
        TypeError: If 'n' is not an instance of int or float representing an integer value.
    """
    # Ensure input is effectively an integer by converting from float if necessary and checking type safety for non-numeric inputs
    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Input must be convertible to a valid integer.")

    return n % 2 != 0

if __name__ == '__main__':
    # Test case 1: Verify that an odd number returns True
    assert is_odd(7) is True
    
    # Test case 2: Verify that an even number returns False
    assert is_odd(4) is False

    print("All sample tests passed.")