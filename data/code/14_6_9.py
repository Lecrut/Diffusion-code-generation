import sys

def is_numeric(value):
    """Check if a string can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_volumes(vol1_str, vol2_str):
    """Compare two volume measurements and print the result."""
    # Validate inputs are numeric
    if not is_numeric(vol1_str) or not is_numeric(vol2_str):
        raise TypeError("Both inputs must be valid numbers.")

    vol1 = float(vol1_str)
    vol2 = float(vol2_str)

    comparison_result = ""
    if vol1 > vol2:
        result_msg = f"{vol1} is greater than {vol2}"
    elif vol1 < vol2:
        result_msg = f"{vol1} is less than {vol2}"
    else:
        result_msg = f"{vol1} equals {vol2}"

    print(result_msg)

def main():
    # Hard-coded sample values as per requirements to avoid input() or sys.stdin calls
    vol_1_measurements = "5.0"
    vol_2_measurements = "3.75"

    try:
        compare_volumes(vol_1_measurements, vol_2_measurements)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()