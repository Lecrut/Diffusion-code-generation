def check_parity(number):
    """
    Determines if a given integer is odd or even.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    sample_numbers = [13, -4, 7, 0]

    for num in sample_numbers:
        result = check_parity(num)
        print(result)