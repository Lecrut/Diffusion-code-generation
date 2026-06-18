def is_odd(n):
    """
    Determines whether a given integer n is odd.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    
    Raises:
        TypeError: If n is not an integer or float representing an integer.
    """
    if isinstance(n, int) and not isinstance(n, bool):
        return n % 2 != 0
    elif isinstance(n, float):
        # Handle cases like 3.5 which should be treated as even (not odd), 
        # but strictly speaking only integers can be "odd". We treat non-int floats as False for safety.
        if int(n) == n:
            return is_odd(int(n))
    else:
        raise TypeError("Input must be an integer or a float representing an integer.")

if __name__ == '__main__':
    # Test case 1: A known odd number
    assert is_odd(7) is True, "Test failed for input 7"
    
    # Test case 2: An even number (including zero and negative numbers)
    assert is_odd(-4) is False, "Test failed for input -4"

    print("All tests passed.")