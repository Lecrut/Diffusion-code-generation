def determine_parity(number):
    """
    Determines if a given integer is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'even' if the number is divisible by 2, otherwise 'odd'.
    """
    return "even" if number % 2 == 0 else "odd"

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or external dependencies.
    test_numbers = [10, 7, -4, 0]

    for num in test_numbers:
        result = determine_parity(num)
        print(f"The number {num} is {result}.")