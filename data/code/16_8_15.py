import sys

def check_positive(number_str: str) -> bool:
    """Check if a string representation of a number is positive."""
    try:
        num = float(number_str)
        return num > 0
    except ValueError:
        # If conversion fails, treat as not positive (or could raise error depending on requirements)
        return False

def main():
    """Process sample input values and print results without user interaction."""
    # Hard-coded sample values to ensure the script runs without external input or files.
    samples = [
        "10",
        "-5",
        "0",
        "3.14",
        "",
        "abc"  # This will trigger a ValueError in conversion, handled gracefully below
    ]

    for sample in samples:
        if not check_positive(sample):
            print(f"{sample}: False")
        else:
            print(f"{sample}: True")

if __name__ == '__main__':
    main()