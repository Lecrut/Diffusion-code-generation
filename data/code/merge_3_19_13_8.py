def is_positive(n: int) -> bool:
    """Return True if n is positive, False otherwise."""
    return n > 0

if __name__ == '__main__':
    # Sample inputs without external interaction or arguments
    test_values = [5, -3, 0]

    for value in test_values:
        result = is_positive(value)
        print(result)