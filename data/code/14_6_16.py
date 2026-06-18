import sys

def is_numeric(s):
    """Check if a string represents a valid number (int or float)."""
    try:
        float(s)
        return True
    except ValueError:
        return False

def compare_values(v1_str, v2_str):
    """Compare two numeric strings and print the result."""
    val1 = float(v1_str)
    val2 = float(v2_str)

    if val1 < val2:
        print(f"{val1} is less than {val2}")
    elif val1 > val2:
        print(f"{val1} is greater than {val2}")
    else:
        print(f"{val1} equals {val2}")

if __name__ == '__main__':
    # Hard-coded sample values for direct execution without external input or files
    volume_1 = "5.0"
    volume_2 = "3.75"

    if is_numeric(volume_1) and is_numeric(volume_2):
        compare_values(volume_1, volume_2)
    else:
        print("Error: Provided values are not numeric.")