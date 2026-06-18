import sys

def check_parity(number: int) -> str:
    """Determine if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    test_values = [1, 4, -3, 0]

    for value in test_values:
        result = check_parity(value)
        print(result)