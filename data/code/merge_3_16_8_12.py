import sys

def is_positive(number: float) -> bool:
    """Check if a number is positive."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or command-line arguments.
    samples = [1, -5, 0, 3.14]

    for num in samples:
        result = is_positive(num)
        print(result)