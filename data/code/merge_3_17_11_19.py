def is_even(number: int) -> bool:
    """Returns True if number is even, False otherwise."""
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [10, -3, 42, 0, 7]
    for val in test_values:
        result = is_even(val)
        print(f"is_even({val}) = {result}")