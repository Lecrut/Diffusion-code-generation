import sys

def check_positive(number_str: str) -> bool:
    """Check if a string representation of a number is positive."""
    try:
        num = float(number_str)
        return num > 0
    except ValueError:
        # If the input cannot be converted to a float, it's not considered positive.
        return False

def main():
    """Process sample inputs and print results without user interaction."""
    # Hard-coded sample values as per requirements (no command-line args or stdin)
    samples = [
        "10",
        "-5",
        "3.14",
        "0",
        "abc",
        "+7"
    ]

    for number_str in samples:
        is_positive = check_positive(number_str)
        print(f"{number_str}: {'Positive' if is_positive else 'Not Positive'}")

if __name__ == '__main__':
    main()