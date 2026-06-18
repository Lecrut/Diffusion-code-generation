import sys

def is_positive_number(user_input):
    """
    Determines if a given string input represents a positive number.
    
    Args:
        user_input (str): The string to check.
        
    Returns:
        bool: True if the number is positive, False otherwise.
    """
    try:
        num = float(user_input)
        return num > 0
    except ValueError:
        # Handle cases where input cannot be converted to a float
        print("Error: Non-numeric input detected.")
        return None

def main():
    """
    Main function containing hard-coded sample values for testing.
    Runs without user interaction or command-line arguments.
    """
    
    test_cases = [
        "10",      # Positive integer
        "-5",       # Negative integer
        "3.14",     # Positive float
        "0",        # Zero (not positive)
        "abc",      # Invalid input
        "",         # Empty string
    ]

    for test_value in test_cases:
        print(f"\nTesting with value: '{test_value}'")
        result = is_positive_number(test_value)
        
        if result is None:
            print("Result: Input could not be processed.")
        elif result:
            print("Result: The number is positive.")
        else:
            print("Result: The number is zero or negative.")

if __name__ == '__main__':
    main()