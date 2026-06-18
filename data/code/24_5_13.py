import sys

def check_number(value):
    """Check if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction
    samples = [1, -5, "not_a_number", 0.5, -3]

    for item in samples:
        try:
            num = int(item)
            is_negative = check_number(num)
            if is_negative:
                print(f"{num} is negative.")
            else:
                print(f"{num} is not negative.")
        except ValueError as e:
            # Handle non-integer input gracefully
            print(f"Error processing '{item}': {e}")