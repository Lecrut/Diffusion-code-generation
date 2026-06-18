def check_zero(value):
    """Check if a value is zero."""
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [0, -5, 3.14, "not an integer", None]

    for item in samples:
        try:
            if isinstance(item, (int, float)):
                num = int(float(item))  # Handle floats like 3.9 -> 3 or exact integers
            else:
                continue
            
            is_zero = check_zero(num)
            
            print(f"Input value: {num}")
            if is_zero:
                print("The entered value is zero.")
            else:
                print("The entered value is not zero.")
        except (ValueError, TypeError):
            # Gracefully handle non-integer or invalid inputs like "not an integer", None, etc.
            print(f"Input '{item}' could not be processed as a valid number for this check.")