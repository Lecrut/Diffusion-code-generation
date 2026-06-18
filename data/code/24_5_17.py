import sys

def check_number(value):
    """Check if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction
    samples = [1, -5, 0, "not_a_number", 42]

    for item in samples:
        try:
            num = int(item)
            if check_number(num):
                print(f"The number {num} is negative.")
            else:
                print(f"The number {num} is not negative.")
        except ValueError as e:
            # Handle cases where input cannot be converted to an integer
            print(f"Error processing '{item}': Non-integer input detected. ({e})")