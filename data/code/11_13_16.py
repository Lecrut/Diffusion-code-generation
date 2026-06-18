import sys

def get_positive_number(prompt):
    """Prompts user (or uses default) to input a positive number."""
    # Since we cannot use interactive prompts or argparse, 
    # this function will be called with either an optional string argument.
    try:
        value = float(value_str if isinstance(value_str := sys.argv[1], str) else 0)
        return value
    except ValueError:
        raise ValueError("Input must be a valid number.")

def validate_positive_number(number):
    """Validates that the input is positive."""
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError(f"Number {number} is not positive. Please enter a value greater than zero.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required for execution.
    
    length_a = 10.5
    length_b = 2
    
    try:
        validate_positive_number(length_a)
        validate_positive_number(length_b)
        
        ratio = length_a / length_b
        
        print(f"Length A ({length_a}) divided by Length B ({length_b}):")
        print("-" * 30)
        print(f"Ratio (A/B): {ratio}")
    except ValueError as e:
        print(e, file=sys.stderr)