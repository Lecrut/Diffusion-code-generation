def check_parity(number):
    """
    Determines if a given integer is odd or even.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    test_values = [1, 42, -3, 0]
    
    for value in test_values:
        result = check_parity(value)
        print(result)