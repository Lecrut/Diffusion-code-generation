def is_positive(n: int) -> bool:
    """Check if a number is positive."""
    return n > 0

if __name__ == '__main__':
    # Sample test cases running without user input or arguments
    sample_values = [5, -3, 0]
    
    for value in sample_values:
        result = is_positive(value)
        print('True' if result else 'False')