import sys

def check_parity(number: int) -> str:
    """Check if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [4, 7, -3, 10]

    for num in test_cases:
        result = check_parity(num)
        print(result)