def is_positive(number: int) -> bool:
    """Return True if number is greater than zero, else False."""
    return number > 0

if __name__ == '__main__':
    sample_values = [1, -5, 0]
    
    for value in sample_values:
        result = is_positive(value)
        print(result)