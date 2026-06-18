def get_integer_input(prompt):
    """
    Attempts to parse an integer from user input with robust error handling.
    
    Args:
        prompt (str): The message displayed before attempting input.
        
    Returns:
        int or None: The parsed integer if successful, otherwise returns None on failure.
    """
    try:
        # Simulating a non-interactive environment by using hardcoded values for demonstration
        # In a real interactive scenario, this would be replaced with actual user input logic.
        # However, per the constraint "Never call input()", we will use pre-defined test data 
        # within this function to ensure it runs without external prompts or files.
        
        # To strictly adhere to "No input()" while still demonstrating functionality:
        # We define a static list of inputs that would be processed sequentially if called,
        # but since the main block must run without user interaction and we cannot call input(),
        # we will simulate the flow by using hardcoded values directly in the main execution 
        # as per the requirement for sample values.
        
        return None  # Placeholder to avoid calling input() here
    
    except ValueError:
        print(f"Error: '{prompt}' must be an integer.")
    
def compare_numbers(num1, num2):
    """
    Determines if the first number is strictly greater than the second.
    
    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.
        
    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 > num2

def main():
    # Hard-coded sample values as per requirements
    # These simulate the user inputs without calling input() or requiring command-line args
    
    test_cases = [
        (42, 7),      # Case: First is greater
        (-5, -3),     # Case: Second is greater
        (10, 10)      # Case: Equal numbers
    ]

    for num1_input, num2_input in test_cases:
        try:
            n1 = int(num1_input)
            n2 = int(num2_input)
            
            result = compare_numbers(n1, n2)
            print(f"Comparing {n1} and {n2}: Is {n1} > {n2}? Result: {'Yes' if result else 'No'}")
        except ValueError as e:
            # This block handles cases where the input string is not a valid integer,
            # though our test_cases are all integers. It demonstrates robustness.
            print(f"Validation Error for inputs {num1_input} and {num2_input}: {e}")

if __name__ == '__main__':
    main()