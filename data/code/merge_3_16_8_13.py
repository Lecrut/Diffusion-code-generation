import sys

def is_positive(number: float) -> bool:
    """Check if a number is strictly positive."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    sample_values = [1, -5, 3.5, 0, 2]

    for value in sample_values:
        result = is_positive(value)
        print(f"{value}: {'Positive' if result else 'Not Positive'}")