def is_odd(n: int) -> bool:
    """Check if an integer is odd using the modulo operator."""
    return n % 2 != 0

if __name__ == '__main__':
    test_values = [1, -3, 4, 0, 7]
    for val in test_values:
        print(f"{val} is {'odd' if is_odd(val) else 'even'}")