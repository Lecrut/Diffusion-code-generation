def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    test_values = [1, 2, -3, 4]

    for value in test_values:
        if is_even(value):
            print(f"{value} is even.")
        else:
            print(f"{value} is odd.")