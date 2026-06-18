import sys

def check_sign(number_str):
    """Check if a string represents a negative integer."""
    try:
        number = int(number_str)
        return number < 0
    except ValueError:
        raise ValueError(f"Input '{number_str}' is not a valid integer.") from None

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction
    sample_values = ["-5", "100", "-3.5", "", "not_a_number", "-7"]

    for value in sample_values:
        try:
            is_negative = check_sign(value)
            if isinstance(is_negative, bool):
                print(f"Number {value} {'is negative' if is_negative else 'is not negative.'}")
            else:
                # Fallback just in case logic changed unexpectedly (shouldn't happen here)
                print("Unexpected result type.")
        except ValueError as e:
            print(f"Error processing '{value}': {e}", file=sys.stderr)