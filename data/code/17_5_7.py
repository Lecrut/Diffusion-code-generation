def check_parity(number):
    """Returns 'Even' if number is even, otherwise returns 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_values = [10, 7, -4, 0]

    for value in test_values:
        result = check_parity(value)
        print(result)