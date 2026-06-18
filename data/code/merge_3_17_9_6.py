def is_even(n: int) -> bool:
    """Check if an integer is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    test_values = [1, 2, -3, 0, 4]

    for value in test_values:
        result = is_even(value)
        print(f"{value} is {'even' if result else 'odd'}")