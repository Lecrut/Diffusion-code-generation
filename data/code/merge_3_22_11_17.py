def is_odd(n: int) -> bool:
    """Return True if n is odd, False otherwise."""
    return n % 2 == 1

if __name__ == '__main__':
    samples = [-5, -4, 0, 3, 789]
    for val in samples:
        print(f"{val}: {is_odd(val)}")