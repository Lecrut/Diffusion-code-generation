import math

def is_even(n: int) -> bool:
    """Check if an integer is even using bitwise AND, which is efficient."""
    return n & 1 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [42, -3, 0, 7, math.inf]

    for num in test_cases:
        try:
            result = is_even(num)
            print(f"{num} is {'even' if result else 'odd'}")
        except TypeError as e:
            # Handle non-integer inputs gracefully while maintaining the function signature's intent
            print(f"Error checking {num}: {e}")