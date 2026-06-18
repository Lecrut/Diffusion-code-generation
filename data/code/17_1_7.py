def is_even(number: int) -> bool:
    """Check if a number is even using the modulo operator."""
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [1, -5, 42, 0]
    for val in test_values:
        result = is_even(val)
        print(f"{val} is {'even' if result else 'odd'}")