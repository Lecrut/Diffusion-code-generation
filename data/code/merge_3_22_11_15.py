def is_odd(number: int) -> bool:
    """Returns True if number is odd, False otherwise."""
    return number % 2 != 0

if __name__ == '__main__':
    test_cases = [-5, -4, 0, 1, 2, 3]
    for val in test_cases:
        print(f"{val} -> {is_odd(val)}")