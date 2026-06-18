def is_positive(number: int) -> bool:
    """Check if a number is positive."""
    return number > 0

if __name__ == '__main__':
    test_values = [1, -5, 0]
    
    for value in test_values:
        result = is_positive(value)
        print(result)