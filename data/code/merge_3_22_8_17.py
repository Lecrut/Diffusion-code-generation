def determine_oddness(number: int) -> bool:
    """Check if a given integer is odd.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0

if __name__ == '__main__':
    # Test case 1: Odd number should return True
    assert determine_oddness(7) is True
    
    # Test case 2: Even number should return False
    assert determine_oddness(8) is False

    print("All test cases passed.")