def is_positive(number: int) -> bool:
    """Return True if number > 0, else False."""
    return number > 0

if __name__ == '__main__':
    test_cases = [1, 0, -5]
    
    for value in test_cases:
        result = is_positive(value)
        
        # Simulate reading from input by printing the result directly.
        print('True' if result else 'False')