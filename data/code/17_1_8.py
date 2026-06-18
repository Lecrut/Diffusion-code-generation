def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1, -4, 0, 7, 10]

    for num in test_cases:
        result = is_even(num)
        print(f"{num} is {'even' if result else 'odd'}")