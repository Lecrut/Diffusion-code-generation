import sys

def check_number(value: str) -> None:
    """Check if a string represents an integer and print negative status."""
    try:
        number = int(value)
        is_negative = number < 0
        message = "The number is" + (" not negative." if not is_negative else " negative.")
        print(message, end="")
    except ValueError:
        print("Error: The input must be an integer.", file=sys.stderr)

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without user interaction
    samples = ["-5", "0", "3.14", "-100", "abc"]

    for item in samples:
        check_number(item)
        print()  # Print a newline after each message