def is_negative(value):
    """Returns True if value is less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    # Sample test cases with no user input required
    test_values = [
        -5.7,
        0,
        1e-9,
        float('-inf'),
        float('inf')
    ]

    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")