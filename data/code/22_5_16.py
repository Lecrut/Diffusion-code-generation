def determine_parity(number: int) -> str:
    """
    Determines if a given integer is odd or even.

    Args:
        number (int): The integer to check.

    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == "__main__":
    # Hard-coded sample values as per constraints (no input() or sys.stdin)
    test_values = [10, -3, 5, 0]

    for val in test_values:
        result = determine_parity(val)
        print(result)