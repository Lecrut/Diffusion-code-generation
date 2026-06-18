def is_odd(n: int) -> bool:
    """Check if an integer is odd."""
    return n % 2 == 1

if __name__ == '__main__':
    test_cases = [0, -5, 3, 42]
    for num in test_cases:
        print(f"{num}: {is_odd(num)}")