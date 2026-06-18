def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [1, -5, 42, 0, 3]
    for num in test_cases:
        result = "Even" if is_even(num) else "Odd"
        print(f"{num} is {result}")