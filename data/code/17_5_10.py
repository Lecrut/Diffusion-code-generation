import sys

def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive input calls.
    test_values = [4, 3, -5, 17]

    for value in test_values:
        if is_even(value):
            print('Even')
        else:
            print('Odd')