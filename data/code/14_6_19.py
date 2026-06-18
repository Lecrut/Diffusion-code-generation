import sys

def validate_numeric(value: str) -> bool:
    """Check if a string represents a valid number (int, float, negative)."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_volumes(vol1_str: str, vol2_str: str) -> str:
    """Compare two volume measurements and print the outcome."""
    if not validate_numeric(vol1_str):
        raise ValueError(f"Invalid numeric value for first measurement: {vol1_str}")
    
    num_val_1 = float(vol1_str)
    
    if not validate_numeric(vol2_str):
        raise ValueError(f"Invalid numeric value for second measurement: {vol2_str}")

    num_val_2 = float(vol2_str)

    print("Result Comparison")
    print("=================")
    print(f"{num_val_1} compared to {num_val_2}")

    if num_val_1 > num_val_2:
        return f"\n{num_val_1} is greater than {num_val_2}"
    elif num_val_1 < num_val_2:
        return f"\n{num_val_1} is less than {num_val_2}"
    else:
        return f"\nThe values are equal"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No external input, arguments, or network access used here.
    measurement_a = "50"       # First volume (liters)
    measurement_b = 25.5      # Second volume

    try:
        result_text = compare_volumes(measurement_a, measurement_b)
        sys.stdout.write(result_text.strip())
        print()
    except ValueError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)