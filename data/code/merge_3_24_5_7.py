import sys

def check_number(value_str):
    """Check if a string represents an integer and print its sign status."""
    try:
        number = int(value_str)
        if number < 0:
            return f"The number {number} is negative."
        else:
            return f"The number {number} is not negative (zero or positive)."
    except ValueError:
        return "Error: The input provided was not a valid integer."

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction.
    samples = ["-5", "0", "10", "-3.5", "abc", "42"]
    
    for item in samples:
        result_message = check_number(item)
        print(result_message)