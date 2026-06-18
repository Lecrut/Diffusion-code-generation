def is_even(n):
    """Check if a number is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    test_values = [1, 2, -3, 4]

    for num in test_values:
        result = is_even(num)
        if result:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")