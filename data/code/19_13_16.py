def is_positive(n: int) -> bool:
    """Check if an integer is positive."""
    return n > 0

if __name__ == '__main__':
    test_cases = [1, -5, 0]
    
    for value in test_cases:
        result = is_positive(value)
        print('True' if result else 'False')