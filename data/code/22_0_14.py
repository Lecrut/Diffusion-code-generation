import sys

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [1, 2, -3, 4]

    for num in test_cases:
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")