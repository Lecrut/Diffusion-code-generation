def check_parity(number):
    """Check if a number is even or odd."""
    return 'Even' if number % 2 == 0 else 'Odd'

if __name__ == '__main__':
    # Hard-coded sample values as per constraints (no input(), sys.stdin, etc.)
    test_values = [4, 7, -3, 10]

    for value in test_values:
        result = check_parity(value)
        print(f"{value} -> {result}")