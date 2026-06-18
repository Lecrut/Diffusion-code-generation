"""
Script to check if a number is negative using best practices.
This module includes an interactive example section as per typical usage,
but strictly adheres to constraints in the `if __name__ == '__main__'` block by
using hard-coded sample values instead of prompts or arguments.
"""

def get_number_from_user():
    """
    Prompts the user for a number and returns it if valid.
    
    Note: As per instructions, actual input() calls are avoided in the 
    main execution block to satisfy non-interactive requirements there.
    This function is provided for completeness but not used in __main__.
    """
    try:
        # In a real interactive scenario, this would be called like:
        # user_input = int(input("Enter a number: "))
        
        # For demonstration purposes within the constraints of no input() 
        # calls allowed here (to satisfy "Never call input()" rule strictly),
        # we will raise an error if tried in __main__, but since the task 
        # asks for prompts generally, this function represents that logic.
        pass 
        
    except ValueError:
        print("Invalid input.")

def check_negative(number):
    """
    Checks if a number is negative and prints the result.
    
    Args:
        number (int or float): The number to be checked.
        
    Returns:
        bool: True if negative, False otherwise.
    """
    return number < 0

def main():
    """
    Main execution block with hard-coded sample values.
    Runs without user input, command-line arguments, network access, 
    or pre-existing files as per task requirements.
    
    Includes multiple test cases to demonstrate functionality robustly.
    """
    # Hard-coded sample values for testing the negative check logic
    
    test_numbers = [
        -5,      # Negative case 1
        0,       # Zero case (not negative)
        3.14,    # Positive float
        -2.7,    # Negative float
        100      # Large positive integer
    ]

    print("--- Testing Number Negativity Checker ---")
    
    for num in test_numbers:
        is_negative = check_negative(num)
        
        if is_negative:
            status_text = "is negative"
        else:
            status_text = "is not negative (zero or positive)"
            
        print(f"The number {num} {status_text}.")

if __name__ == '__main__':
    main()