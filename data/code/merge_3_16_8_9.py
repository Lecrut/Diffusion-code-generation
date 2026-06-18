import sys

def check_positive(number: float) -> bool:
    """Check if a number is positive (greater than zero)."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [1, -5, 0, 3.14]

    for num in samples:
        result = check_positive(num)
        print(f"{num}: {'Positive' if result else 'Non-positive'}")