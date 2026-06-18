def check_parity(number):
    """
    Determines if a given integer is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to be checked.
        
    Returns:
        str: 'Even' if the number is divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or external dependencies.
    test_numbers = [10, 7, -4, 0]
    
    for num in test_numbers:
        result = check_parity(num)
        print(f"The number {num} is {result}.")