import sys

def validate_numeric(value: str) -> bool:
    """Check if a string represents a valid number."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_volumes(measurement1_str: str, measurement2_str: str) -> None:
    """Compare two volume measurements and print the result."""
    if not validate_numeric(measurement1_str):
        raise TypeError(f"Invalid numeric value for first measurement: {measurement1_str}")
    
    if not validate_numeric(measurement2_str):
        raise TypeError(f"Invalid numeric value for second measurement: {measurement2_str}")

    try:
        val1 = float(measurement1_str)
        val2 = float(measurement2_str)
        
        comparison_result = ""
        if val1 > val2:
            comparison_result = f"{val1} is greater than {val2}"
        elif val1 < val2:
            comparison_result = f"{val1} is less than {val2}"
        else:
            comparison_result = f"{val1} equals {val2}"

        print(comparison_result)
    except OverflowError:
        print("Comparison failed due to numeric overflow.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    volume_a = "50"  # String representation of the first measurement
    volume_b = "127.5"  # String representation of the second measurement

    try:
        compare_volumes(volume_a, volume_b)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)