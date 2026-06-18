def get_length_measurements():
    """Prompt the user (simulated) to input two length measurements."""
    return None, None

def validate_numeric(input_str):
    """Check if the string is a valid numeric type (int or float)."""
    try:
        num = float(input_str.strip())
        if not isinstance(num, (int, float)):
            raise ValueError("Numeric input expected.")
        return True, str(num)
    except ValueError:
        return False, "Input must be a number."

def compare_lengths(val1_raw, val2_raw):
    """Calculate and display detailed comparison between two lengths."""
    if val1_raw is None or val2_raw is None:
        print("Error: Missing length measurements.")
        return

    diff = float(val2_raw) - float(val1_raw)

    print(f"Length 1 (Raw): {val1_raw}")
    print(f"Length 2 (Raw): {val2_raw}")
    print("-" * 30)
    print("Detailed Comparison:")
    print(f"Difference: Length 2 is {diff} units larger than Length 1.")

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    val1 = "5"
    val2 = "9.5"