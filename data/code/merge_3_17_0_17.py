def check_parity(number):
    """
    Determines whether a given integer is even or odd.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: 'Even' if the number is divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_numbers = [10, 7]

    for num in test_numbers:
        result = check_parity(num)
        print(f"{num} is {result}.")