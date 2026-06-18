def read_weight(input_str):
    """Converts a string to float with error handling."""
    try:
        return float(input_str)
    except ValueError as e:
        raise RuntimeError(f"Invalid weight input '{input_str}': {e}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no user input needed)
    val1 = "75.5"
    val2 = "80.3"

    try:
        w1 = read_weight(val1)
        w2 = read_weight(val2)
        difference = abs(w2 - w1)
        print(f"{difference:.1f}")  # Print formatted to one decimal place for clarity
    except RuntimeError as error:
        print(error, file=__import__('sys').stderr)