def is_even(n: int) -> bool:
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [10, -3, 42, 0]
    for val in test_values:
        print(f"is_even({val}) = {is_even(val)}")