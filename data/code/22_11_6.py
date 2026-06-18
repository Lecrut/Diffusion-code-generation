def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.
    
    Uses bitwise AND with 1 to check the least significant bit efficiently.
    This avoids division operations which are computationally more expensive.
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if n is odd, False if even or non-integer input (though type hint ensures int)
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [0, 1, -3, 42, -7]
    
    print("Testing is_odd function:")
    for num in test_cases:
        result = is_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num}: {status}")