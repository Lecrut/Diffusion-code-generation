def is_positive(n: int) -> bool:
    """Return True if n is positive, False otherwise."""
    return n > 0

if __name__ == '__main__':
    # Sample values to test the logic without user input.
    sample_values = [5, 0, -3]

    for value in sample_values:
        result = is_positive(value)
        print('True' if result else 'False')