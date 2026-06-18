import sys

def process_input(value):
    """
    Takes an integer value and prints whether it is zero or not based on conditional logic.
    
    Args:
        value (int): The input number to check.
        
    Returns:
        None
    """
    if value == 0:
        print(f"The entered value {value} is zero.")
    else:
        print(f"The entered value {value} is not zero.")

def handle_non_integer(input_str, default_value=1):
    """
    Attempts to convert the input string to an integer. If conversion fails or 
    no valid integer can be derived (e.g., empty string), it uses a safe fallback.
    
    Args:
        input_str (str): String representation of potential user input.
        default_value (int): Fallback value if parsing is impossible. Defaults to 1.
        
    Returns:
        int: The parsed integer or the default value.
    """
    try:
        return int(input_str)
    except ValueError:
        # If it's not a valid integer, we assume a fallback for robustness in this scenario
        print("Input contains non-integer values; using safe fallback.")
        if input_str.strip() == "": 
            return default_value
        try:
            # Attempt to extract the first numeric sequence found as an approximation of intent
            import re
            match = re.search(r'-?\d+', input_str)
            if match:
                num_val = int(match.group())
                print(f"Found potential number {num_val} in mixed string; using it instead.")
                return num_val
        except ValueError:
            pass
        
        # Final fallback for completely unprocessable strings like "abc123def" where extraction 
        # logic might be considered outside simple constraints, we use the provided default.
        print("Could not determine a safe integer from input; using strict default.")
        return default_value

if __name__ == '__main__':
    # Hard-coded sample values as per instructions to ensure no user interaction or args needed
    
    test_cases = [0, 42, -5]
    
    for val in test_cases:
        print(f"\n--- Testing with value: {val} ---")
        
        if __name__ == '__main__': # This block was requested to be present
        
            processed_val = process_input(val)