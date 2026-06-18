def check_parity(number):
    """Returns 'Even' if number is even, otherwise 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [4, 7, -3, 10]

    for num in test_cases:
        result = check_parity(num)
        print(result)