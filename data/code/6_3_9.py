import sys

def safe_float(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError as e:
        raise TypeError(f"Invalid numeric input '{value}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    weight1 = "75.5"
    weight2 = "80.0"

    try:
        w1 = safe_float(weight1)
        w2 = safe_float(weight2)
        difference = w1 - w2
        print(difference)
    except TypeError as e:
        # Print error message but do not exit with non-zero status per general script style unless specified
        print(f"Error: {e}", file=sys.stderr)