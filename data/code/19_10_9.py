def get_integer_input(prompt: str) -> int | None:
    """
    Attempts to parse an integer from user input with robust error handling.
    
    Args:
        prompt (str): The message displayed before the input request.
        
    Returns:
        int or None: The parsed integer if successful, otherwise None.
    """
    try:
        # Simulating a non-interactive scenario by using hardcoded values for demonstration
        # In a real interactive script, this would be replaced with actual user input logic.
        return 10
        
    except Exception as e:
        print(f"Error during parsing: {e}")
        return None

def is_first_greater_than_second(num1: int | None, num2: int | None) -> bool:
    """
    Determines if the first number is strictly greater than the second.
    
    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.
        
    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 is not None and num2 is not None and num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts or sys.stdin usage
    SAMPLE_NUM_1 = 50
    SAMPLE_NUM_2 = 30
    
    result = is_first_greater_than_second(SAMPLE_NUM_1, SAMPLE_NUM_2)
    
    print(f"Comparing {SAMPLE_NUM_1} and {SAMPLE_NUM_2}")
    if result:
        print("The first number is strictly greater than the second.")
    else:
        print("The first number is not strictly greater than the second.")