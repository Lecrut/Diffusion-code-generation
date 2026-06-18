import sys

def check_number(value):
    """Check if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction
    sample_values = [1, -5, 0, "not_a_number", 42]

    for item in sample_values:
        try:
            num = int(item)
            if check_number(num):
                print(f"{num} is negative.")
            else:
                print(f"{num} is not negative.")
        except ValueError as e:
            # Handle non-integer input gracefully without printing error messages to stdout
            pass