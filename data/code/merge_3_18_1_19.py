def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    result1 = is_greater(10.5, 7.3)
    print(f"Test case 1: {result1}")

    result2 = is_greater(-5, -9)
    print(f"Test case 2: {result2}")

    result3 = is_greater(42, 42)
    print(f"Test case 3: {result3}")