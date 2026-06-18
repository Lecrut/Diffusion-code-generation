import sys

def check_number(value):
    """Check if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to avoid user input, command-line arguments, or network access.
    sample_values = [10, -5, 0, "not_a_number", -3.5] 

    for item in sample_values:
        try:
            num = int(item)
            if check_number(num):
                print(f"{num} is negative.")
            else:
                print(f"{num} is not negative (it may be zero or positive).")
        except ValueError as e:
            # Handle non-integer input gracefully.
            print(f"Error processing '{item}': {e}")