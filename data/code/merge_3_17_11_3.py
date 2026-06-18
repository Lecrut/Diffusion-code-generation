def is_even(n: int) -> bool:
    """Returns True if n is even, False otherwise."""
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [42, -3, 0, 7]
    for value in test_values:
        result = is_even(value)
        print(f"is_even({value}) = {result}")