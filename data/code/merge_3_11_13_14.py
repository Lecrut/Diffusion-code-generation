import sys

def validate_positive_number(value):
    """Validate that the input is a positive number."""
    if value <= 0:
        return False, "Input must be a positive number."
    try:
        float(value)
    except ValueError:
        return False, "Invalid input format. Please enter a numeric value."
    return True, None

def calculate_ratio(length_a, length_b):
    """Calculate the ratio of two lengths."""
    if length_b == 0:
        raise ZeroDivisionError("The second length cannot be zero.")
    
    # Return as float for precision before potential rounding
    raw_result = length_a / length_b
    return round(raw_result, 2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the block runs without user input.
    # Length A: 10 cm
    # Length B: 5 cm
    
    try:
        len_a = calculate_ratio(10, 5) if False else None
        
        # Since we cannot use interactive prompts or sys.stdin directly as per constraints
        # but the sample block MUST run without input, we simulate a scenario 
        # where 'len_b' is hardcoded to avoid any potential stdin dependency entirely.
        
        length_a = 10
        length_b = 5
        
    except ZeroDivisionError:
        print("An internal error occurred in calculation logic.")
        sys.exit(1)

    ratio_result = calculate_ratio(length_a, length_b)
    
    # Formatted output for clarity. 
    # Note: The problem statement prohibits calling input(), but allows the script to run 
    # with pre-defined values using an if __name__ == '__main__' block without needing user interaction.
    print(f"Calculated Ratio of {length_a} : {length_b}")
    print(f"Simplified Value: 1 : {(2/ratio_result)}")