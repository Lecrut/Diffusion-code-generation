import math

def is_even(n: int) -> bool:
    """Check if an integer is even using bitwise AND operation."""
    return n & 1 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [2, -3, 0, 10**5]

    for num in test_cases:
        print(f"Is {num} even? {is_even(num)}")