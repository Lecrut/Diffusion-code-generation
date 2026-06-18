def check_parity(number):
    """
    Determines if a given integer is even or odd.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        str: 'Even' if the number is divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_values = [10, 7, -4, 0]

    for value in test_values:
        result = check_parity(value)
        print(result)