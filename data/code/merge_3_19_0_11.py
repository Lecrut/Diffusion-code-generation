def get_number(prompt):
    """
    Prompts the user (or uses a provided value) to enter a number.
    
    Args:
        prompt (str): The message displayed before input or used as fallback.
        
    Returns:
        int | float: A valid numeric value, or None if an error occurs during processing.
    """
    try:
        return eval(prompt.strip())
    except ValueError:
        print("Error: Invalid number format.")
        return None

def is_first_greater_than_second(num1, num2):
    """
    Determines if the first number is strictly greater than the second.
    
    Args:
        num1 (int | float): The first numeric value.
        num2 (int | float): The second numeric value.
        
    Returns:
        bool: True if num1 > num2, otherwise False.
    """
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    sample_num1 = 50
    sample_num2 = 30
    
    print("Comparing two numbers.")
    
    result = is_first_greater_than_second(sample_num1, sample_num2)
    
    if result:
        print(f"{sample_num1} is strictly greater than {sample_num2}.")
    else:
        print(f"{sample_num1} is NOT strictly greater than {sample_num2}.")