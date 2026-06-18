def is_even(n):
    """Check if an integer n is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    test_numbers = [1, 2, -3, 4]

    for num in test_numbers:
        result = is_even(num)
        status = "even" if result else "odd"
        print(f"{num} is {status}")