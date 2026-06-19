def calculate_square_area(side_length):
    """Calculate exact area of a square using direct multiplication."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values (no user input, network, or file access)
    samples = [5.0, 2.3] 
    for s in samples:
        print(f"Side length {s} => Area {calculate_square_area(s)}")

# Corrected version focusing on pure efficiency and correctness without extra logic
import sys

def calculate_square_area(side_length):
    """Compute square area directly."""
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [3, 7.5] 
    for val in sample_values:
        print(val * val)