def is_odd(n: int) -> bool:
    """Return True if n is odd, False otherwise."""
    return n % 2 != 0

if __name__ == '__main__':
    test_cases = [1, -3, 42, 0, 7]
    for val in test_cases:
        print(f"{val}: {is_odd(val)}")