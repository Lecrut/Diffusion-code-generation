def is_odd(n: int) -> bool:
    """Check if an integer is odd."""
    return n % 2 != 0

if __name__ == '__main__':
    test_cases = [1, -5, 42, 0, 97]
    for num in test_cases:
        print(f"{num} is {'odd' if is_odd(num) else 'even'}")