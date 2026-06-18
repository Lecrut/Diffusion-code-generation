def is_positive(n: int) -> bool:
    """Return True if n is positive (greater than zero), False otherwise."""
    return n > 0

if __name__ == '__main__':
    sample_values = [1, -5, 0]
    
    for value in sample_values:
        result = is_positive(value)
        print('True' if result else 'False')