def different_numbers(a: int | float, b: int | float) -> bool:
    """Yields True if two input numbers are different, False otherwise."""
    return a != b

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    tests = [
        (10, 20),      # Should yield True
        (5.5, 6.5),    # Should yield True
        (42, 42),      # Should yield False
        (-3, -3),      # Should yield False
        (0, 0),        # Should yield False
        (1e-4, 1e-4), # Float equality check
    ]

    for num1, num2 in tests:
        result = different_numbers(num1, num2)
        print(f"Numbers {num1} and {num2}: Different={result}")