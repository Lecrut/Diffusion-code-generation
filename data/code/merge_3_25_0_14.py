def is_zero(number):
    """Check if a given number is exactly zero."""
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [1, -5.0, 0, "0", True]

    for value in samples:
        try:
            num_value = float(value) if isinstance(value, str) else value
            result = is_zero(num_value)
            print(f"Input {value} -> Is exactly zero? {result}")
        except (ValueError, TypeError):
            # Handle cases where conversion or comparison fails gracefully
            print(f"Input {value} -> Invalid type for numeric check")