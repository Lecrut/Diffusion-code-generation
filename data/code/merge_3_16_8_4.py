import sys

def is_positive(number: float) -> bool:
    """Check if a number is strictly positive."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [1, -5, 0, 3.14, "invalid"]

    for item in samples:
        try:
            num = float(item)
            result = is_positive(num)
            print(f"{item} -> {'positive' if result else 'not positive'}")
        except ValueError:
            # Handle cases where input cannot be converted to a number.
            print(f"{item} -> invalid number")