def determine_parity(number: int) -> str:
    """
    Determines whether a given integer is odd or even.

    Args:
        number (int): The integer to check.

    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_numbers = [1, 4, -3, 0]

    for num in test_numbers:
        result = determine_parity(num)
        print(f"The number {num} is {result}.")