import sys

def parse_weight(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError as e:
        raise RuntimeError(f"Invalid weight input '{value}': {e}") from None

if __name__ == '__main__':
    # Hard-coded sample values instead of user input
    w1_str = "70.5"
    w2_str = "68.3"
    
    try:
        w1 = parse_weight(w1_str)
        w2 = parse_weight(w2_str)
        
        difference = abs(w1 - w2)
        print(f"{difference:.1f}")
    except RuntimeError as e:
        # Error handling for non-numeric input in sample block (though inputs are hard-coded here)
        sys.exit(1)