import sys

def process_number(line: str) -> None:
    """Process a single input line to check if it is positive."""
    try:
        number = float(line.strip())
        # Check if the number is strictly greater than zero
        result = "Positive" if number > 0 else "Not Positive (zero or negative)"
        print(result)
    except ValueError as e:
        print(f"Error processing input '{line}': {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction
    samples = [
        "10",
        "-5.5",
        "0",
        "3.14",
        "",  # Empty string test
        "abc"  # Invalid number test
    ]

    for sample in samples:
        process_number(sample)