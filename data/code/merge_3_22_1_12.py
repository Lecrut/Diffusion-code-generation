def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is odd, False if even or non-integer input type passed directly as arg.
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [1, -3, 42, 0, 7]
    
    print("Testing is_odd function:")
    for num in test_cases:
        result = is_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num} -> {status}")