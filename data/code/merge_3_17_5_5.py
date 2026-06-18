def determine_parity(number):
    """Returns 'Even' if number is even, otherwise returns 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_values = [4, 7, -3, 18]

    for value in test_values:
        result = determine_parity(value)
        print(f"{value}: {result}")