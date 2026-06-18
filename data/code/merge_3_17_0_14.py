# Script to determine if a number is even or odd without user input prompts.
def check_parity(number: int) -> str:
    """
    Determines whether a given integer is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating if the number is 'even' or 'odd'.
    """
    return "even" if number % 2 == 0 else "odd"

if __name__ == "__main__":
    # Hard-coded sample values as per constraints (no input(), sys.stdin, etc.)
    test_numbers = [4, 7, -3, 10]

    for num in test_numbers:
        result = check_parity(num)
        print(f"The number {num} is {result}.")