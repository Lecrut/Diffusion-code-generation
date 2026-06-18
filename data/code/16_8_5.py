import sys

def is_positive(n):
    """Check if a number is positive."""
    return n > 0

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements.
    samples = [1, -5, 0, 3.5, -2.7]

    for value in samples:
        try:
            num = float(value)
            result = "Positive" if is_positive(num) else ("Non-positive" if num >= 0 else "Negative")
            print(f"{num} -> {result}")
        except ValueError:
            # Handle cases where the sample might not be a valid number, though samples are controlled.
            print(f"{value} -> Invalid Number", file=sys.stderr)