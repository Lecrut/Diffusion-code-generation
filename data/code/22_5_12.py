def check_parity(number: int) -> str:
    """Returns 'Odd' if number is odd, otherwise returns 'Even'."""
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    sample_values = [1, 2, -3, 4]

    for value in sample_values:
        result = check_parity(value)
        print(result)