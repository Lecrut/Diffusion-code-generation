def is_zero(value):
    """Returns True if value is zero (0), False otherwise."""
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -1, 1, 3.5, 0.0, "zero", None]
    for val in test_cases:
        result = is_zero(val) if isinstance(val, (int, float)) else False
        print(f"is_zero({val}) -> {result}")