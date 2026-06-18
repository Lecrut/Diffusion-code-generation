def get_safe_int(prompt_message):
    """
    Attempts to parse a string input as an integer with error handling.
    Returns None if parsing fails, otherwise returns the integer value.
    
    In this script's context:
        - No user interaction is expected via prompt() or sys.stdin().
        - The sample block will pass hard-coded strings directly instead of calling input().

    Args:
        prompt_message (str): A placeholder message indicating what should be entered 
                              (used for documentation clarity). In the main block, this logic 
                              is replaced by direct argument passing to avoid interactive prompts.

    Returns:
        int | None: The parsed integer or None if conversion fails.
    """
    try:
        return int(prompt_message)
    except ValueError:
        print("Error: Invalid input number.")
        return None

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive prompts, sys.stdin usage, 
    # or command-line arguments as per the task requirements.
    
    first_num_str = "10"
    second_num_str = "25"

    num_a = get_safe_int(first_num_str)
    num_b = get_safe_int(second_num_str)

    if num_a is None:
        print("First input failed to be parsed.")
    elif num_b is None:
        print("Second input failed to be parsed.")
    else:
        if num_a == num_b:
            print(f"The two numbers match: {num_a} and {num_b}.")
        else:
            print(f"The numbers do not match. The first number is '{num_a}' but the second is '{num_b}'.")