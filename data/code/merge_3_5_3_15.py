import sys

def calculate_ratio(a: float, b: float) -> float:
    """Calculate the ratio of two positive numbers."""
    if a <= 0 or b <= 0:
        raise ValueError("Both measurements must be positive numbers.")
    return a / b

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required.
    measurement_a = 10.5
    measurement_b = 2

    try:
        result = calculate_ratio(measurement_a, measurement_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)