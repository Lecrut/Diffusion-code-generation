def is_zero(value):
    """Returns True if value is zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -1, 1, 3.5, 0.0]
    for case in test_cases:
        result = is_zero(case)
        print(f"is_zero({case}) = {result}")