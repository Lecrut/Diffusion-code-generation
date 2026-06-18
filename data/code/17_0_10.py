"""
Script to determine if an integer is even or odd.

This script defines a function that checks the parity of an integer 
and returns 'even' or 'odd'. It includes a main execution block with 
hard-coded sample values to demonstrate functionality without requiring user input.
"""

def check_parity(number: int) -> str:
    """
    Determines whether a given integer is even or odd.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: 'even' if the number is divisible by 2, otherwise 'odd'.
    """
    return "even" if number % 2 == 0 else "odd"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration. 
    # No user input, command-line arguments, or external dependencies are used.
    
    test_numbers = [42, -3, 17]

    print("Checking parity of the following numbers:")
    for num in test_numbers:
        result = check_parity(num)
        print(f"The number {num} is {result}.")