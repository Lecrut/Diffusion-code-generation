def print_parity(number):
    """Prints 'Even' if number is even, otherwise prints 'Odd'."""
    return "Even" if (number % 2 == 0) else "Odd"

if __name__ == '__main__':
    sample_values = [4, 7, -3, 10]

    for value in sample_values:
        result_message = print_parity(value)
        print(result_message)