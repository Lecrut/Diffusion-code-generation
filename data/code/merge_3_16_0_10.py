import sys

def is_positive_number(user_input: str) -> bool:
    """Check if a string representation of a number is positive."""
    try:
        # Attempt to convert input to float first (handles decimals and scientific notation), then check sign.
        num = float(user_input.strip())
        return num > 0
    except ValueError:
        raise ValueError(f"Invalid numeric input: '{user_input}'. Please enter a valid number.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction.
    test_cases = [
        "123",      # Positive integer
        "-456",     # Negative integer
        "0",        # Zero (not positive)
        "7.89",     # Positive float
        "-abc",     # Non-numeric string error case 1
        "   ",      # Whitespace only error case
    ]

    for test_value in test_cases:
        try:
            result = is_positive_number(test_value)
            print(f"Input '{test_value}' -> Is Positive? {result}")
        except ValueError as e:
            print(e)