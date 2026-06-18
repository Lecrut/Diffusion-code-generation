def safe_float(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError as e:
        raise ValueError(f"Invalid numeric input '{value}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or arguments.
    w1_str = "75.5"
    w2_str = "80.3"

    try:
        weight_1 = safe_float(w1_str)
        weight_2 = safe_float(w2_str)
        difference = abs(weight_1 - weight_2)
        print(f"Difference: {difference}")
    except ValueError as e:
        # The error message will indicate which input was invalid.
        raise