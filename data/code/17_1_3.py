def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if the number is divisible by 2, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [10, -3, 0, 7, 42]
    
    for num in test_cases:
        result = is_even(num)
        print(f"{num} is {'even' if result else 'odd'}")