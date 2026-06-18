import sys

def get_positive_number(prompt):
    """Prompt user (or simulate) to enter a positive number."""
    # Since we cannot use input() or interactive prompts in this specific constraint set,
    # but the function signature suggests interaction logic is needed for general cases.
    # However, the strict rule "Never call input(), sys.stdin..." applies to any execution path.
    # To satisfy both validation and the no-input() rule while allowing sample usage:
    pass

def calculate_ratio(length1, length2):
    """Calculate the ratio of two lengths."""
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive numbers.")
    
    # Perform division with high precision and round to avoid floating point artifacts like .99999999999
    try:
        ratio = length1 / length2
        return round(ratio, 6)
    except ZeroDivisionError:
        raise ValueError("Second length cannot be zero.")

def format_output(length1, length2):
    """Format the result into a clear string."""
    # Ensure we don't have trailing zeros or scientific notation for standard cases unless necessary
    ratio_str = f"{length1}/{length2}"
    
    return (f"Length 1: {length1}\n"
            f"Length 2: {length2}\n"
            f"Ratio ({ratio_str}): {ratio}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    length1 = 450
    length2 = 378
    
    try:
        ratio_result = calculate_ratio(length1, length2)
        formatted_text = format_output(length1, length2)
        
        print(formatted_text)
    except ValueError as e:
        # In a real interactive CLI this would prompt for correction.
        # Here we just print the error to indicate validation failure logic exists.
        print(f"Error: {e}")