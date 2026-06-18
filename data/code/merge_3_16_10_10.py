def is_positive(number: int) -> bool:
    """Returns True if number is greater than zero."""
    return number > 0

if __name__ == '__main__':
    # Sample values to test without user interaction
    test_values = [5, -1, 0]
    
    for value in test_values:
        result = is_positive(value)
        print(f"{value} is {'positive' if result else 'not positive'}")