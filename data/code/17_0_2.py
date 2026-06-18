def check_parity(number):
    """
    Determines if a given integer is even or odd.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: 'Even' if the number is divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Test cases with hard-coded sample values.
    # No user input, command-line arguments, or network access is used here.
    test_numbers = [10, -3, 42]

    for num in test_numbers:
        result_status = check_parity(num)
        print(f"The number {num} is {result_status}.")