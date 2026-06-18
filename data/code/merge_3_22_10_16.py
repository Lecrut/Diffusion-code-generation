"""
Module to determine if an integer is odd or even using the modulo operator.

This script defines a function that takes an integer input, checks its parity 
using the modulo (%) operator, and returns 'odd' or 'even'. The main execution block 
contains hard-coded sample values for demonstration purposes without requiring user interaction.
"""

def check_parity(number: int) -> str:
    """
    Determines whether a given integer is odd or even.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    
    Examples:
        >>> check_parity(5)
        'odd'
        >>> check_parity(4)
        'even'
    """
    # Use modulo operator to check divisibility by 2. 
    # If remainder is 0, the number is even; otherwise, it's odd.
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == '__main__':
    sample_values = [13, -4, 0, 7]

    for val in sample_values:
        result = check_parity(val)
        print(f"The number {val} is {result}.")