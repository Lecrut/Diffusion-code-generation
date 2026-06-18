import sys

def parse_weight(value):
    """Convert a string to float."""
    try:
        return float(value)
    except ValueError as e:
        raise TypeError(f"Invalid weight value '{value}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    weights = [75.0, 82.5]
    
    try:
        w1 = parse_weight(weights[0])
        w2 = parse_weight(weights[1])
        
        difference = abs(w1 - w2)
        print(f"{difference:.2f}")
    except (IndexError, TypeError):
        # Handles cases where input list is too short or contains non-numeric strings.
        sys.exit(1)