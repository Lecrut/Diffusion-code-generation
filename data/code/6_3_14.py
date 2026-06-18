def parse_weight(value_str):
    """Convert a string to float with error handling."""
    try:
        return float(value_str)
    except ValueError:
        raise ValueError(f"Invalid weight value: {value_str}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed)
    weight1 = "50.5"
    weight2 = "48.3"

    try:
        w1_float = parse_weight(weight1)
        w2_float = parse_weight(weight2)
        difference = abs(w1_float - w2_float)
        print(f"{difference}")
    except ValueError as e:
        # Handle non-numeric input gracefully without crashing the script entirely
        print(f"Error: {e}", file=__import__('sys').stderr)