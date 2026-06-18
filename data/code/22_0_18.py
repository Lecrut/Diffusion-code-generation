# Determine if a number is odd or even based on user input logic.
# Note: Per instructions, no interactive prompts (input()) will be used in execution flow.
# This module defines helper functions and includes a test block with hard-coded values.

def check_parity(number):
    """
    Determines whether the given integer is odd or even.

    Parameters:
        number (int): The integer to evaluate.

    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_values = [17, 42, -3, 0]

    for value in test_values:
        result = check_parity(value)
        print(f"The number {value} is {result}.")