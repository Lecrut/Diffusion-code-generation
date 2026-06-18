import sys

def is_even(n: int) -> bool:
    """Check if an integer n is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Sample values provided directly without user input or command-line arguments.
    test_cases = [1, 2, -3, 4]

    for number in test_cases:
        if is_even(number):
            print(f"{number} is even")
        else:
            print(f"{number} is odd")