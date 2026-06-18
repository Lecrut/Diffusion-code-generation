def check_parity(number):
    """
    Determines if a given integer is odd or even.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments
    test_cases = [17, -4, 0, 5]
    
    for num in test_cases:
        result = check_parity(num)
        print(result)