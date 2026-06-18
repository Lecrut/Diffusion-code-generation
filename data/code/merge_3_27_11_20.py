def get_number(prompt):
    """
    Prompts the user (or uses a provided value) to enter a number, 
    converting it safely with error handling.
    
    Args:
        prompt (str): The message displayed before input request if interactive mode is used.
        
    Returns:
        int or float: A valid numeric value entered by the user or sample data.
    """
    while True:
        try:
            # In a non-interactive context, this might just be passed directly 
            # to avoid blocking on input() calls in environments without stdin.
            # Here we attempt standard conversion; if an exception occurs during evaluation,
            # it will be caught by the caller or handled via sample values below.
            value = eval(prompt)  # Using eval for simplicity with potential expressions like "10" to handle strings/int/float
            
        except Exception:
            print("Invalid input. Please enter a valid number.")
            continue
        
        return int(value) if isinstance(value, (int, float)) else value

def check_difference(num1, num2):
    """
    Checks if two numbers are different.
    
    Args:
        num1 (number): First numeric value.
        num2 (number): Second numeric value.
        
    Returns:
        bool: True if the values differ, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access.
    sample_num1 = 42
    sample_num2 = 8
    
    print("Comparing numbers...")

    try:
        result = check_difference(sample_num1, sample_num2)
        
        if result:
            print(f"{sample_num1} and {sample_num2} are different.")
        else:
            print(f"{sample_num1} and {sample_num2} are the same.")

    except Exception as e:
        # Graceful error handling for unexpected issues during calculation.
        print(f"An error occurred while checking values: {e}")