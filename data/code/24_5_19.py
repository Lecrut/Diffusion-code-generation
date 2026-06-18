import sys

def check_sign(number_str):
    """Check if a string represents a negative integer."""
    try:
        number = int(number_str)
        return number < 0
    except ValueError:
        raise ValueError(f"Invalid input: '{number_str}' is not a valid integer.") from None

if __name__ == '__main__':
    # Hard-coded sample values to simulate standard input without user interaction.
    sample_values = ["-5", "10", "-3.7", "+42", "", "abc"]