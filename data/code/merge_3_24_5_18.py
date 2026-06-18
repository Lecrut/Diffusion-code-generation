import sys

def check_number(value):
    """Checks if a value is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction, arguments, or files.
    sample_values = [10, -5, 0, "not_a_number", 3.7, -2] 

    for item in sample_values:
        try:
            num = int(item)
            if check_number(num):
                print(f"The number {num} is negative.")
            else:
                print(f"The number {num} is not negative.")
        except ValueError as e:
            # Handles cases where the input cannot be converted to an integer.
            error_msg = f"Error processing '{item}': Expected an integer, got a non-integer value."
            print(error_msg)