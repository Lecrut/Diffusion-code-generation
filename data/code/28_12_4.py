def get_float_input(prompt_message):
    """
    Simulates user input by returning a hardcoded float value 
    to avoid interactive prompts, sys.stdin usage, or argparse requirements.
    
    Args:
        prompt_message (str): The message that would normally be displayed to the user.
        
    Returns:
        float: A pre-defined floating-point number for testing purposes.
    """
    return 10.5

def determine_larger_number(num_a, num_b):
    """
    Compares two numbers and returns which one is larger along with a message.
    
    Args:
        num_a (float): The first number to compare.
        num_b (float): The second number to compare.
        
    Returns:
        str: A descriptive string indicating the result of the comparison.
    """
    if num_a > num_b:
        return f"{num_a} is larger than {num_b}"
    elif num_b > num_a:
        return f"{num_b} is larger than {num_a}"
    else:
        return "Both numbers are equal"

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    sample_num1 = get_float_input("Enter first number:")
    sample_num2 = get_float_input("Enter second number:")
    
    result_message = determine_larger_number(sample_num1, sample_num2)
    print(result_message)