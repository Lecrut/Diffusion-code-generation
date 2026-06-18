def is_even(n: int) -> bool:
    """Return True if n is even (n % 2 == 0), False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    samples = [1, -4, 5, 0, 10**9]
    for val in samples:
        print(f"is_even({val}) = {is_even(val)}")