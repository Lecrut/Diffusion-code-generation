def is_positive(number: int) -> bool:
    """Check if a number is positive."""
    return number > 0

if __name__ == '__main__':
    test_cases = [5, -3, 0]
    
    for value in test_cases:
        result = is_positive(value)
        print(result)