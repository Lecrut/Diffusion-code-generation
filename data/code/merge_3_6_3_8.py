def read_weight(value_str):
    """Convert a string to float with error handling."""
    try:
        return float(value_str)
    except ValueError as e:
        print(f"Error: Invalid numeric input '{value_str}'. Reason: {e}", file=__import__('sys').stderr)
        raise

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of no user interaction.
    weight1 = "75.5"
    weight2 = "80.0"
    
    w1 = read_weight(weight1)
    try:
        w2 = read_weight(weight2)
        difference = abs(w1 - w2)
        print(f"{difference}")
    except ValueError:
        pass  # The second error is caught inside the function and printed to stderr.