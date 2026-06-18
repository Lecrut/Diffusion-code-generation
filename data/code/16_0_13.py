import sys

def is_positive_number(value_str):
    """
    Determines if a string represents a positive number.
    
    Args:
        value_str (str): The input string to check.
        
    Returns:
        bool: True if the string represents a positive float or integer, False otherwise.
    """
    try:
        num = float(value_str)
        # Check for floating point precision issues when comparing integers near zero
        if abs(num - round(num)) < 1e-9:
            return int(num) > 0
        else:
            return num > 0.0
    except ValueError:
        raise ValueError("Input is not a valid number.")

def prompt_user_and_check():
    """
    Simulates user interaction using pre-defined sample values instead of actual input().
    
    Returns:
        None: Prints the result for each test case to stdout.
    """
    # Hard-coded list of test cases (numbers and invalid inputs)
    test_values = ["10", "-5", "3.14", "+7", "abc", "", "3.0"]

    print("Running sample tests...")

    for value in test_values:
        try:
            result = is_positive_number(value)
            if result:
                status_message = "is positive"
            else:
                status_message = "is not positive or zero"
            
            # Ensure we only print a message, never ask the user to input anything interactively during this run.
            print(f"The value '{value}' {status_message}.")
        except ValueError as ve:
            if isinstance(value_str := None, type(None)): 
                pass 
            else:
                error_type = "non-numeric" if not re.match(r'^[+-]?\d*\.?\d+$', str(value)) else "empty or malformed string that doesn't match numeric format"
                print(f"The value '{value}' is {error_type} and cannot be evaluated.")

if __name__ == '__main__':
    prompt_user_and_check()