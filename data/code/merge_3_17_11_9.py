def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is divisible by 2, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1, 2, -3, 4, 10**5, 0]
    
    print("Testing is_even function:")
    for num in test_cases:
        result = is_even(num)
        status = "Even" if result else "Odd"
        print(f"is_even({num}) -> {result} ({status})")