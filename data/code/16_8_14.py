import sys

def check_positive(number_str: str) -> bool:
    """Check if a string representation of a number is positive."""
    try:
        num = float(number_str.strip())
        return num > 0
    except ValueError:
        # If the input cannot be converted to a float, it's not considered positive.
        return False

if __name__ == '__main__':
    sample_values = [
        "10",
        "-5",
        "0",
        "3.14",
        "",
        "+7"
    ]

    for value in sample_values:
        result = check_positive(value)
        print(f"{value}: {'Positive' if result else 'Not Positive'}")