def is_negative(value):
    """Returns True if value is less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    test_cases = [-1, -3.5, 0, 42]
    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")