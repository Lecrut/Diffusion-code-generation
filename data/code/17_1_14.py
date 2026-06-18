def is_even(n: int) -> bool:
    """
    Check if an integer is even using the modulo operator.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if n is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [10, -3, 42, -7]
    for num in test_cases:
        result = is_even(num)
        print(f"{num} is {'even' if result else 'odd'}")