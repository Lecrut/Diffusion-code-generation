def is_even(n: int) -> bool:
    """Check if a number is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [-5, -4, 3, 100, 9876]
    for num in test_cases:
        result = is_even(num)
        print(f"{num} is {'even' if result else 'odd'}")