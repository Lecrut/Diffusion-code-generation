def determine_parity(number):
    """
    Determines if a given integer is odd or even using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    """
    return "odd" if number % 2 else "even"

if __name__ == '__main__':
    # Sample test values run without user input or external dependencies.
    sample_values = [5, -3, 0, 18]

    for value in sample_values:
        result = determine_parity(value)
        print(f"The number {value} is {result}.")