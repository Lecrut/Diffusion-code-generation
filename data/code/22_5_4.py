def check_parity(number):
    """
    Determines if a given integer is odd or even.
    
    Args:
        number (int): The integer to be checked.
        
    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_values = [1, 2, -3, 4]

    for value in test_values:
        result = check_parity(value)
        print(result)