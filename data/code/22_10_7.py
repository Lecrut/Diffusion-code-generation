def determine_parity(number: int) -> str:
    """
    Determines whether a given integer is odd or even using the modulo operator.

    Args:
        number (int): The integer to check.

    Returns:
        str: "Odd" if the number is not divisible by 2, otherwise "Even".
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input.
    test_values = [1, -3, 4, 0]

    for num in test_values:
        result = determine_parity(num)
        print(f"The number {num} is {result}.")