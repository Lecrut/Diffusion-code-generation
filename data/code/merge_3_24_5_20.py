import sys

def check_negative(number_str: str) -> bool:
    """Check if a string represents a negative integer."""
    try:
        number = int(number_str)
        return number < 0
    except ValueError:
        # Non-integer input detected, treat as error condition for this task context
        raise

def process_input():
    """Process integers read from standard input and print status."""

if __name__ == '__main__':
    pass
