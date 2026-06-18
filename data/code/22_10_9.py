def is_odd_or_even(number):
    """
    Determines if a given integer is odd or even using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: A string indicating whether the number is 'odd' or 'even'.
    """
    remainder = number % 2
    
    if remainder == 0:
        return "even"
    else:
        return "odd"

if __name__ == '__main__':
    # Sample values to test without user input, command-line arguments, 
    # network access, or pre-existing files.
    
    sample_numbers = [1, -2, 0, 45]

    for num in sample_numbers:
        result = is_odd_or_even(num)
        print(f"The number {num} is {result}.")