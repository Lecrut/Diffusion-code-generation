def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [10, 7, -4, 0, 3]
    for val in test_values:
        print(f"{val}: {is_even(val)}")