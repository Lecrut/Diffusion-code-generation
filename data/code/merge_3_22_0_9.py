# Script to determine if a number is odd or even without user input interaction.
# This module demonstrates parity checking using hard-coded sample values.

def check_parity(number: int) -> str:
    """
    Determines whether an integer is odd or even.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: A string indicating if the number is 'odd' or 'even'.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, network access, or file I/O is used.

    test_numbers = [1, 2, -3, 4]

    print("Parity Check Results:")
    for num in test_numbers:
        result = check_parity(num)
        print(f"The number {num} is {result}.")