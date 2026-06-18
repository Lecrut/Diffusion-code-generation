import sys

def check_number(value):
    """Checks if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to simulate input without user interaction
    sample_values = [1, -5, 0, "not_a_number", 3.5] 

    for item in sample_values:
        try:
            num = int(item)
            if check_number(num):
                print(f"The number {num} is negative.")
            else:
                print(f"The number {num} is not negative (it is non-negative).")
        except ValueError:
            # Handles cases where input cannot be converted to an integer
            print("Error: The provided value could not be interpreted as an integer.")