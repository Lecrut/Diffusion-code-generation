import sys

def is_positive_number(value):
    """Check if a number is positive."""
    try:
        num = float(value)
        return num > 0, str(num)
    except ValueError:
        raise TypeError("Input must be numeric.") from None

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or network access.
    test_cases = ["10", "-5", "3.14", "abc", "", " 7 "]

    for case in test_cases:
        try:
            positive, result_str = is_positive_number(case)
            print(f"Input '{case}' -> Positive: {positive}, Value as float: {result_str}")
        except TypeError as e:
            print(f"Error processing input '{case}': {e}", file=sys.stderr)