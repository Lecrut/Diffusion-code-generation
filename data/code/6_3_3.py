import sys

def parse_weight(value):
    """Parse a weight value from string to float."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Error: '{value}' is not a valid number.")

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user input, no args)
    weight1_str = "75.5"
    weight2_str = "68.3"

    try:
        weight1 = parse_weight(weight1_str)
        weight2 = parse_weight(weight2_str)
        
        difference = weight1 - weight2
        
        print(f"{weight1} and {weight2}: Difference is {difference}")
    
    except ValueError as e:
        # Error handling for non-numeric input or other value-related errors
        sys.stdout.write(str(e)) + "\n"