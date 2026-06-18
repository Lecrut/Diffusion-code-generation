def check_parity(number: int) -> str:
    """
    Determines if a number is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'Even' if divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid input() or sys.stdin calls.
    test_values = [10, 7, -4, 3]
    
    for val in test_values:
        result = check_parity(val)
        print(f"{val} is {result}")