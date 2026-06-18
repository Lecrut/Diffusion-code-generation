def determine_parity(number):
    """
    Determines if a given integer is odd or even using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Sample values to test without user input or command-line arguments.
    sample_values = [1, -3, 4, 0]

    for num in sample_values:
        result = determine_parity(num)
        print(f"The number {num} is {result}.")