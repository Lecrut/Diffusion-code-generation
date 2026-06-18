def is_positive(n: int) -> bool:
    """Return True if n is positive, False otherwise."""
    return n > 0

if __name__ == '__main__':
    # Sample values to test without user input or command-line arguments.
    sample_values = [5, -3, 0]

    for value in sample_values:
        result = is_positive(value)
        print('True' if result else 'False')