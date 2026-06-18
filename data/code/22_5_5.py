def get_parity(number):
    """Returns 'Odd' if number is odd, otherwise returns 'Even'."""
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [1, 4, -3, 0]

    for num in test_cases:
        result = get_parity(num)
        print(result)