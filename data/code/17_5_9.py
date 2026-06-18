def check_parity(number):
    """Returns 'Even' if number is even, otherwise returns 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments.
    test_values = [4, 7, -3, 10]

    for value in test_values:
        result = check_parity(value)
        print(result)