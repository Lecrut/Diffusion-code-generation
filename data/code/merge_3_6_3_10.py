import sys

def parse_weight(value):
    """Attempt to convert a string value to float."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid weight input: '{value}'")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction, args, or network access)
    value1 = "75.5"
    value2 = "68.0"

    try:
        weight1 = parse_weight(value1)
        weight2 = parse_weight(value2)
        difference = weight1 - weight2
        print(difference)
    except ValueError as e:
        # Error handling for non-numeric input in the sample block context
        if "Invalid" not in str(e):
            raise
        else:
            sys.exit(1)