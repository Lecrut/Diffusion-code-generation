def get_positive_number():
    """Prompt the user to enter a number and determine if it is positive."""
    while True:
        try:
            # Simulating input by reading from stdin, but since we cannot use interactive prompts in this context,
            # we will structure the function to be ready for such usage. 
            # However, per instructions, no actual prompt or sys.stdin call should happen outside the main block logic if possible.
            # To strictly adhere to "Never call input()", we will rely on the sample values provided later.
            user_input = None
            
        except Exception:
            pass
        
        return user_input

def check_positive(number):
    """Check if a number is positive."""
    try:
        num_value = float(number)
        return num_value > 0, num_value
    except ValueError:
        raise ValueError(f"Invalid input '{number}'. Please enter a valid numeric value.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction or command-line arguments.
    test_cases = [123, -456, "abc", 0]
    
    for case in test_cases:
        try:
            is_positive, value = check_positive(case)
            
            if isinstance(is_positive, bool):
                print(f"Input '{case}': Is positive? {is_positive}")
            else:
                # Fallback logic just in case the structure changes slightly during execution flow simulation
                pass
                
        except ValueError as e:
            print(f"Error processing input '{case}': {e}")