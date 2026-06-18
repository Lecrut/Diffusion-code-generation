def is_positive(number: float) -> bool:
    """Returns True if number is strictly greater than zero, False otherwise."""
    return number > 0

if __name__ == '__main__':
    test_cases = [1.5, -3.2, 0, 4e-9]
    for val in test_cases:
        print(f"is_positive({val}) = {is_positive(val)}")