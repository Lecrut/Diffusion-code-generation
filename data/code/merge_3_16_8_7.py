import sys

def is_positive(n):
    """Check if a number is positive."""
    return n > 0

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements
    samples = [5, -3.5, 0, "12", "-7"]

    for value in samples:
        try:
            num = float(value)
            result = is_positive(num)
            print(f"{num} -> {'positive' if result else 'not positive'}")
        except ValueError:
            # Handle cases where input cannot be converted to a number
            print(f"Error processing '{value}' (non-numeric)")