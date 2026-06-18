def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n % 2 != 0

if __name__ == '__main__':
    test_values = [1, -3, 42, 0, 7]
    
    for val in test_values:
        result = is_odd(val)
        print(f"is_odd({val}) = {result}")