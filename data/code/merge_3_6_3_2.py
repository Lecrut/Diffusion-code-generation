def read_weight(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError as e:
        raise RuntimeError(f"Invalid weight value '{value}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    val1 = "75.5"
    val2 = "80.3"

    try:
        weight_a = read_weight(val1)
        weight_b = read_weight(val2)
        difference = weight_a - weight_b
        print(difference)
    except RuntimeError as e:
        # Print error message to stderr if input conversion fails, though inputs are hardcoded here.
        import sys
        print(f"Error: {e}", file=sys.stderr)