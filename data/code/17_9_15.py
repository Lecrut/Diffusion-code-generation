def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    samples = [42, -3, 17, 0]
    for val in samples:
        print(f"{val} is {'even' if is_even(val) else 'odd'}")