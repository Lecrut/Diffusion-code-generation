def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if the number is odd, False if even or not an integer.
    """
    return n % 2 != 0

if __name__ == '__main__':
    test_cases = [1, -3, 42, 0, 7]
    
    for case in test_cases:
        result = is_odd(case)
        print(f"is_odd({case}) = {result}")