import sys

def check_negative(number: float) -> bool:
    """Check if a given number is negative."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [10, -5, 0]

    for num in test_cases:
        result = check_negative(num)
        print(f"Is {num} negative? {'Yes' if result else 'No'}")