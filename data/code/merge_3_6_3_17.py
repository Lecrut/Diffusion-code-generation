def convert_to_float(value):
    """Convert a string to float."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid numeric input: {value}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction needed).
    weight1_str = "70.5"
    weight2_str = "68.3"

    try:
        weight1 = convert_to_float(weight1_str)
        weight2 = convert_to_float(weight2_str)
        difference = weight1 - weight2
        print(difference)
    except ValueError as e:
        # Error handling for non-numeric input.
        print(f"Error: {e}")