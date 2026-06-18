def get_float_value(value_str):
    """Converts a string to float. Raises ValueError if conversion fails."""
    try:
        return float(value_str)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid numeric input provided: {value_str}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    weight1 = "75.5"
    weight2 = "80.3"

    try:
        w1 = get_float_value(weight1)
        w2 = get_float_value(weight2)
        difference = w2 - w1
        print(difference)
    except ValueError as e:
        # Print error message but continue gracefully or exit with code 0 for non-interactive scripts
        pass