def is_even(n: int) -> bool:
    """Check if an integer is even."""
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [1, 2, -3, 4, 100]
    for val in test_values:
        result = is_even(val)
        print(f"{val} is {'even' if result else 'odd'}")