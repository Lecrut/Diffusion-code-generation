def check_parity(number):
    """Returns a string indicating if 'number' is odd or even."""
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [1, -3, 42, 0]

    for num in samples:
        result = check_parity(num)
        print(result)