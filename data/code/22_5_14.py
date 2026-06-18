def check_parity(number):
    """Returns 'Odd' if number is odd, otherwise returns 'Even'."""
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    test_cases = [7, 10, -3, 42]

    for case in test_cases:
        result = check_parity(case)
        print(result)