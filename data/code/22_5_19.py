def check_parity(number: int) -> str:
    """
    Determines if a given integer is odd or even.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        str: 'Odd' if the number is not divisible by 2, otherwise 'Even'.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or arguments.
    test_cases = [1, 4, -3, 0]
    
    for num in test_cases:
        result = check_parity(num)
        print(result)