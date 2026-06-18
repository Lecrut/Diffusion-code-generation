def check_parity(n: int) -> str:
    """
    Determines if an integer is even or odd using the modulo operator.
    
    Args:
        n (int): The number to check.
        
    Returns:
        str: 'Even' if divisible by 2, otherwise 'Odd'.
    """
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == '__main__':
    test_numbers = [4, 7, -12, 3]

    for num in test_numbers:
        result = check_parity(num)
        print(f"{num} is {result}")