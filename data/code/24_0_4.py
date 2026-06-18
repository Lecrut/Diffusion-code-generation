import sys

def check_number_negative(user_input: str) -> bool:
    """
    Attempts to convert user input to a float and checks if it is negative.
    
    Args:
        user_input (str): String representation of the number entered by the user.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
            
    Raises:
        ValueError: If the input string cannot be converted to a float.
    """
    try:
        num = float(user_input)
        return num < 0
    except (ValueError, TypeError):
        raise

if __name__ == '__main__':
    # Sample values for testing without requiring user input or command-line arguments.
    test_cases = [
        "-5",      # Should be negative
        "10",       # Should not be negative
        "-3.14",   # Negative float
        "0",        # Zero is neither positive nor negative
        "",         # Empty string to test robustness (will raise error)
    ]

    for case in test_cases:
        try:
            result = check_number_negative(case)
            if result:
                print(f"'{case}' IS NEGATIVE")
            else:
                print(f"'{case}' is NOT negative or zero.")
        except ValueError as e:
            # Silently handle invalid inputs in this specific robustness context
            # to demonstrate error handling without crashing the script unexpectedly.
            pass