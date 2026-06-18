import sys

def check_positive(number_str: str) -> bool:
    """Check if a string representation of a number is positive."""
    try:
        num = float(number_str.strip())
        return num > 0
    except ValueError:
        return False

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or files.
    samples = [
        "123",
        "-456",
        "0",
        "+789",
        "abc",
        "  -10 ",
        "3.14"
    ]

    for sample in samples:
        is_positive = check_positive(sample)
        print(f"{sample} -> {'Positive' if is_positive else 'Not Positive'}")