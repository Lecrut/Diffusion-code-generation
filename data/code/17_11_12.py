def is_even(n: int) -> bool:
    """
    Check if an integer is even.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [10, -3, 42, 0, 7]
    
    for num in samples:
        result = is_even(num)
        print(f"is_even({num}) = {result}")