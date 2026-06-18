def is_positive(n: int) -> bool:
    """Return True if n is positive, False otherwise."""
    return n > 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [10, -5, 0]

    for value in samples:
        result = is_positive(value)
        print(str(result).lower())