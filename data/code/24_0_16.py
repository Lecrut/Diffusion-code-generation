import sys

def check_negative(number: float) -> bool:
    """Check if a given number is negative."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [1, -5, 0, 3.14]

    for num in test_cases:
        is_negative = check_negative(num)
        print(f"Number {num} is negative? {is_negative}")