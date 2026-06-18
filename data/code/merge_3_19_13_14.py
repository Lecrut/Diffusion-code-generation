def check_positive(n: int) -> bool:
    """Return True if n is positive, False otherwise."""
    return n > 0

if __name__ == '__main__':
    test_values = [5, -3, 0]
    
    for value in test_values:
        result = check_positive(value)
        print(result)