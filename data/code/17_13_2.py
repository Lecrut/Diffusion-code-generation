def is_even(n: int) -> bool:
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [10, -3, 42, 0]
    for case in test_cases:
        print(f"is_even({case}) =", is_even(case))