# python_odd_even_checker.py

import sys
    
def check_parity(number: int) -> None:
    """
    Determines whether a given integer is odd or even and prints the result.
    
    A number is considered even if it can be divided by 2 with no remainder (modulo == 0).
    Otherwise, it is classified as odd.
    
    Args:
        number (int): The integer to check for parity
        
    Prints a descriptive message indicating whether 'number' is odd or even.
    """
    if number % 2 == 0:
        print(f"The integer {number} is Even.")
    else:
        print(f"The integer {number} is Odd.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or command-line arguments.
    
    samples = [1, 2, -3, 0]
    
    for val in samples:
        check_parity(val)