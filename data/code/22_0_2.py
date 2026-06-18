# Script to determine if an integer is odd or even without user interaction via input().
# This module demonstrates parity checking using a sample block that runs autonomously.

def check_parity(number):
    """
    Determines whether the given integer is odd or even.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        str: A string indicating 'odd' if the number is not divisible by 2, 
             and 'even' otherwise.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    # These values ensure the script runs immediately upon execution in any environment.
    
    test_numbers = [1, -3, 42, 0]

    for num in test_numbers:
        result_type = check_parity(num)
        print(f"The number {num} is {result_type}.")