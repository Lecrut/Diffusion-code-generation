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
    test_cases = [10, -3, 42, 0, 7]
    
    results = []
    for num in test_cases:
        result = is_even(num)
        results.append(f"is_even({num}) -> {result}")
    
    # Print all results to stdout (no interactive input required)
    print("\n".join(results))