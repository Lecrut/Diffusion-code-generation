def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [1, 2, -3, 4, 0]
    for num in test_cases:
        print(f"{num} is {'even' if is_even(num) else 'odd'}")