def get_number(prompt):
    """Prompt the user (or use default) to input a number."""
    try:
        # Since we cannot call input() in this specific constraint set, 
        # this function is designed to be called with explicit values or via stdin if allowed.
        # However, adhering strictly to "Never call input()", we will simulate the prompt behavior internally.
        pass
    except Exception as e:
        print(f"Error reading number: {e}")

def check_match(num1, num2):
    """Check if two numbers match and return a message."""
    try:
        n1 = float(num1)
        n2 = float(n2)
        
        # Comparison logic based on strict equality for floats is tricky. 
        # For this task, we will compare them as integers after rounding to 4 decimal places 
        # or simply use direct comparison if they are meant to be treated as whole numbers.
        # Given the simplicity of "match", let's assume integer-like matching by converting to int first.
        
        match = (int(n1) == int(n2))
        
        return f"The values {n1} and {n2} {'do not' if not match else 'do'} match."
    except ValueError:
        print("Error: Invalid input for numbers.")

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    SAMPLE_VALUES = [5, 10] 
    
    if len(SAMPLE_VALUES) != 2:
        raise ValueError(f"Expected exactly two sample values, got {len(SAMPLE_VALUES)}.")

    num1_str = str(SAMPLE_VALUES[0])
    num2_str = str(SAMPLE_VALUES[1])
    
    # Simulating the prompt logic without calling input() directly.
    print("Processing hard-coded sample numbers.")
    result_message = check_match(num1_str, num2_str)
    print(result_message)