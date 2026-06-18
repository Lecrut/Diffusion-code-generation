def is_positive(number: float) -> bool:
    """Returns True if number is strictly greater than zero, False otherwise."""
    return number > 0

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    test_cases = [5.5, -3, 0.0, float('inf'), float('-inf')]

    for val in test_cases:
        result = is_positive(val)
        print(f"is_positive({val}) = {result}")