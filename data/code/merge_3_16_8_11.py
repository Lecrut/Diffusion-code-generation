import sys

def check_positive(number: float) -> bool:
    """Check if a number is positive."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    sample_values = [1, -5, 0, 3.14, -2]

    for num_str in map(str, sample_values):
        try:
            number = float(num_str)
            is_positive = check_positive(number)
            print(f"Number {num_str}: Positive={is_positive}")
        except ValueError:
            # In case the hard-coded value cannot be converted to a valid number.
            continue