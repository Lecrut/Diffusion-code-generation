def check_parity(number: int) -> str:
    """
    Determines if a given integer is odd or even using the modulo operator.

    Parameters:
        number (int): The integer to check.
    
    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    """
    remainder = number % 2
    return "odd" if remainder != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or network access.
    test_numbers = [17, 42, -3, 0]

    for num in test_numbers:
        result = check_parity(num)
        print(f"The number {num} is {result}.")