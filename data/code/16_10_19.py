def is_positive(value):
    """Return True if value > 0 else False."""
    return value > 0

if __name__ == '__main__':
    # Sample values to test without user input or command-line arguments
    sample_values = [5, -3, 0, "12", None]

    for val in sample_values:
        try:
            num = int(val) if not isinstance(val, (int, float)) else val
            result = is_positive(num)
            print(f"Input {val} -> Value: {num}, Is Positive?: {result}")
        except ValueError as e:
            # Handles non-integer inputs like strings that can't be converted to int
            print(f"Error processing input {val}: Non-integer or invalid type.")