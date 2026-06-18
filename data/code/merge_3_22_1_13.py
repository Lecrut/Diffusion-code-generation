def is_odd(number: int) -> bool:
    """Check if a number is odd using the modulo operator."""
    return number % 2 != 0

if __name__ == '__main__':
    test_cases = [1, -3, 42, 0, 7]
    for num in test_cases:
        result = is_odd(num)
        print(f"{num} is {'odd' if result else 'even'}")