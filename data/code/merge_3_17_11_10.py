def is_even(number: int) -> bool:
    """Returns True if 'number' is even, False otherwise."""
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, -5, 42, -18, 3]
    for val in test_values:
        print(f"is_even({val}) = {is_even(val)}")