import sys

def process_number(number: int) -> str:
    """Check if a number is positive and return the result."""
    if number > 0:
        return "Positive"
    else:
        return "Non-positive"

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input.
    samples = [5, -3, 0]

    for num in samples:
        result = process_number(num)
        print(result)