def is_negative(value):
    """Returns True if value is strictly less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    test_cases = [
        (-5),
        (0),
        (3.14),
        (-2.7e-8),
        float('-inf'),
        float('inf')
    ]

    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")