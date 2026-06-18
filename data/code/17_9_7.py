def is_even(number: int) -> bool:
    """Check if a given integer is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to verify functionality without user input or external dependencies.
    test_values = [1, -5, 42, 999]

    for value in test_values:
        if is_even(value):
            print(f"{value} is even.")
        else:
            print(f"{value} is odd.")