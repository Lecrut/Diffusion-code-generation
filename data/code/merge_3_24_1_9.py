def is_negative(value):
    """Return True if value is less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    test_cases = [5, -3.14, 0, float('-inf'), float('inf')]
    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")