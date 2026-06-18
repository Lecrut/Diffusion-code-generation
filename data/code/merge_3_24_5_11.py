import sys

def check_number(value):
    """Check if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements
    sample_values = [1, -5, 0, "not_a_number", 3.14] 

    for item in sample_values:
        try:
            num = int(item)
            if check_number(num):
                print(f"{num} is negative.")
            else:
                print(f"{num} is not negative (it may be zero or positive).")
        except ValueError as e:
            # Handle cases where input cannot be converted to an integer
            error_msg = f"Error processing '{item}': {e}"
            if isinstance(item, str):
                print(error_msg)
            else:
                print(f"{error_msg}")