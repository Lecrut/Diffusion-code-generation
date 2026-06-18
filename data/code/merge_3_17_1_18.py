def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [1, -5, 42, 0]
    for val in test_values:
        result = is_even(val)
        print(f"{val} is {'even' if result else 'odd'}")