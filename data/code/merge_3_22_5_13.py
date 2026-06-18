def get_parity(n: int) -> str:
    """
    Determines if an integer is odd or even.
    
    Args:
        n (int): The number to check
        
    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise
    """
    return "Odd" if n % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [17, 42, -3, 0]
    
    for num in test_cases:
        result = get_parity(num)
        print(f"{num}: {result}")