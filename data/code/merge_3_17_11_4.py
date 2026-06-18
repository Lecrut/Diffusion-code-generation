def is_even(n: int) -> bool:
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    samples = [10, -3, 5, 0, 7]
    for val in samples:
        print(f"{val}: {is_even(val)}")