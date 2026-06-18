def is_even(number):
    """Check if a number is even using the modulo operator."""
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or network access.
    test_numbers = [1, 2, -3, 4, 5]

    for num in test_numbers:
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")