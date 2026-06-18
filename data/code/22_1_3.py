def is_odd(n: int) -> bool:
    """Return True if n is odd, False otherwise."""
    return n % 2 != 0

if __name__ == '__main__':
    samples = [10, -3, 42, -5]
    for s in samples:
        result = is_odd(s)
        print(f"is_odd({s}) = {result}")