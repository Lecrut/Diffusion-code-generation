import sys

def check_number(value: str) -> None:
    """Check if a string represents an integer and print its sign status."""
    try:
        num = int(value)
        if num < 0:
            print(f"{value} is negative.")
        else:
            print(f"{value} is not negative (zero or positive).")
    except ValueError:
        print(f"Error: '{value}' is not a valid integer.", file=sys.stderr)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input, command-line arguments, 
    # network access, or pre-existing files.
    samples = ["-5", "0", "123", "-99", "abc"]

    for item in samples:
        check_number(item)