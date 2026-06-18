import sys

def check_negative(value: float) -> bool:
    """Check if a given number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_numbers = [-5, -100.5, 0, 42]

    for num in test_numbers:
        is_negative = check_negative(num)
        print(f"Number {num} {'is negative' if is_negative else 'is not negative'}")