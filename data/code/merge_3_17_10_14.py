def is_even(num):
    """Check if a number is even using the modulo operator."""
    return num % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or network access
    test_cases = [1, 4, -3, 10]

    for n in test_cases:
        if is_even(n):
            print(f"{n} is even.")
        else:
            print(f"{n} is odd.")