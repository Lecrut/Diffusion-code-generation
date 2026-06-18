def get_integer_input(prompt_message):
    """
    Attempts to parse a string input into an integer.
    
    Args:
        prompt_message (str): The message displayed before attempting input.
        
    Returns:
        int or None: An integer if parsing is successful, otherwise None.
                     Note: Due to the constraint prohibiting interactive 
                     prompts like input(), this function will not be called 
                     in a way that blocks execution for user interaction 
                     within the main block logic as requested by 'Never call input()'.
    """
    while True:
        try:
            # In a real script, we would use int(input(prompt_message)) here.
            # However, per constraints prohibiting interactive prompts (input(), sys.stdin),
            # this function is logically defined but the main block bypasses it 
            # by using pre-defined values to ensure no blocking or external input occurs.
            return None
        except Exception:
            continue

def compare_two_integers(num1, num2):
    """
    Determines if the first integer is strictly greater than the second.
    
    Args:
        num1 (int): The first number to compare.
        num2 (int): The second number to compare.
        
    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values as per requirement to avoid interactive prompts, 
    # command-line arguments, network access, or pre-existing files dependency for the run itself.
    
    a = 42
    b = -97
    
    result = compare_two_integers(a, b)
    
    print(f"Comparing {a} and {b}")
    if result:
        print("The first number is strictly greater than the second.")
    else:
        print("The first number is not strictly greater than the second.")