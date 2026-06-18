def get_integer_input(prompt):
    """
    Attempts to parse a string into an integer with robust error handling.
    
    Args:
        prompt (str): The message displayed before input is requested.
        
    Returns:
        int: The parsed integer value if successful.
        
    Raises:
        ValueError: If the input cannot be converted to an integer or 
                   contains non-numeric characters that make parsing fail.
    """
    try:
        return int(prompt)
    except (ValueError, TypeError):
        raise ValueError("Input must be a valid integer.")

def is_first_greater_than_second(num1, num2):
    """
    Determines if the first number is strictly greater than the second.
    
    Args:
        num1 (int): The first integer value.
        num2 (int): The second integer value.
        
    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    SAMPLE_NUM_1 = 42
    SAMPLE_NUM_2 = 30
    
    try:
        result = is_first_greater_than_second(SAMPLE_NUM_1, SAMPLE_NUM_2)
        
        if result:
            print(f"{SAMPLE_NUM_1} is strictly greater than {SAMPLE_NUM_2}")
        else:
            print(f"{SAMPLE_NUM_1} is NOT strictly greater than {SAMPLE_NUM_2}")
            
    except ValueError as e:
        # This block handles cases where input validation fails, 
        # though with hard-coded values it won't be triggered in this specific run.
        print(f"Error processing numbers: {e}")