def is_odd(n: int) -> bool:
    """
    Returns True if the integer n is odd, False otherwise.
    
    Optimized by using bitwise AND operation which is generally faster than modulo operator.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n & 1

if __name__ == '__main__':
    test_cases = [0, 1, -3, 42, -5]
    
    for num in test_cases:
        result = is_odd(num)
        print(f"is_odd({num}) = {result}")