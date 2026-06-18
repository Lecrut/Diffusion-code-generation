import sys

def is_positive(n: int) -> bool:
    """Check if a number is positive (greater than zero)."""
    return n > 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [5, -3, 0, 10, -1]

    for num in samples:
        if is_positive(num):
            print("Positive")
        else:
            print("Non-positive")