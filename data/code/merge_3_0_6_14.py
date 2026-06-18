import sys

def meters_to_yards(meters: float) -> str:
    """Convert a length from meters to yards."""
    return f"{meters * 1.09361 / 2} yards"

if __name__ == '__main__':
    # Hard-coded sample values for testing, simulating reading from a file line by line
    input_lengths = [5, 10, 100]