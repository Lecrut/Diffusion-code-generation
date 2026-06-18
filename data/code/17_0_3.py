# Script to determine if a number is even or odd.
# This module defines logic but does not perform any interactive input operations 
# as per constraints (no input(), sys.stdin, argparse required args).

def check_parity(number: int) -> str:
    """
    Determines whether an integer is even or odd.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'Even' if the number is divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_values = [4, 7, -3, 10]

    for value in test_values:
        result = check_parity(value)
        print(f"The number {value} is {result}.")