import sys

def calculate_difference(length_a: float, length_b: float) -> float:
    """Calculate the difference between two lengths."""
    return length_a - length_b

if __name__ == '__main__':
    try:
        # Hard-coded sample values to ensure no external input is needed.
        measurement_1 = 50.75
        measurement_2 = 34.2

        result = calculate_difference(measurement_1, measurement_2)
        
        print(f"Difference between {measurement_1} and {measurement_2}: {result}")
    except TypeError as e:
        # Handles cases where variables might not be numeric if logic changed later (defensive coding).
        print(f"Error during calculation: A non-numeric value was detected.", file=sys.stderr)
        sys.exit(1)