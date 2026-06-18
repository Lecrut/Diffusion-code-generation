import sys

def determine_parity(number: int) -> str:
    """Returns 'Even' if number is even, otherwise 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    test_values = [10, 7, -3, 4]

    for val in test_values:
        result = determine_parity(val)
        print(result)