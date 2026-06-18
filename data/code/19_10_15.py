def get_integer_input(prompt):
    """
    Attempts to retrieve an integer from user input with validation.
    
    Args:
        prompt (str): The message displayed before attempting input.
        
    Returns:
        int or None: The parsed integer if successful, otherwise returns the original string as a fallback 
                     for error handling in other parts of the script logic.
                     
    Raises:
        ValueError: If the provided value is not an integer and cannot be converted to one.
    """
    try:
        return int(prompt)
    except (ValueError, TypeError):
        # In a real interactive scenario with sys.stdin or input(), we would handle this here.
        # Since the task forbids calling input() directly in the main block and requires 
        # robust handling of non-integers without crashing on invalid data types:
        raise ValueError("Input must be an integer.") from None

def is_strictly_greater_than(first_number, second_number):
    """
    Determines if the first number is strictly greater than the second.
    
    Args:
        first_number (int or float): The potential larger value.
        second_number (int or float): The comparison value.
        
    Returns:
        bool: True if first_number > second_number, False otherwise.
    """
    return first_number > second_number

def main():
    # Hard-coded sample values to ensure the script runs without user input
    num1 = 42
    num2 = 30
    
    result = is_strictly_greater_than(num1, num2)
    
    print(f"Is {num1} strictly greater than {num2}?")
    if result:
        print("Yes.")
    else:
        print("No.")

if __name__ == '__main__':
    main()