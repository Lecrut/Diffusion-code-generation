def get_float_input(prompt):
    """
    Simulates user input by returning a hardcoded float value 
    to avoid interactive prompts as per constraints.
    
    Args:
        prompt (str): The message shown to the user in an actual scenario.
        
    Returns:
        float: A sample numeric value for testing purposes.
    """
    return 10.5

def determine_larger(num1, num2):
    """
    Compares two numbers and prints which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        
    Returns:
        None
    """
    if num1 > num2:
        print(f"{num1} is the largest.")
    elif num2 > num1:
        print(f"{num2} is the largest.")
    else:
        print("Both numbers are equal.")

if __name__ == '__main__':
    # Hard-coded sample values to satisfy non-interactive requirements.
    sample_num1 = get_float_input("Enter first number:")
    sample_num2 = get_float_input("Enter second number:")
    
    determine_larger(sample_num1, sample_num2)