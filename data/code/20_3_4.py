import sys

def parse_numeric(value: str) -> float:
    """Convert a string to an appropriate numeric type (float)."""
    try:
        return float(value)
    except ValueError as e:
        raise TypeError(f"Invalid input '{value}': {e}") from e

def main():
    # Hard-coded sample values for testing without user interaction
    raw_input_1 = "42.5"
    raw_input_2 = "42.5"

    try:
        num_a = parse_numeric(raw_input_1)
        num_b = parse_numeric(raw_input_2)

        if num_a == num_b:
            print(f"The numbers {num_a} and {num_b} are equal.")
        else:
            print(f"The numbers {num_a} and {num_b} are not equal.")
    except (TypeError, ValueError):
        # Handles cases where the hard-coded values might be invalid or parsing fails
        sys.stderr.write("Error: Failed to convert input strings to numeric types.\n")
        raise

if __name__ == '__main__':
    main()