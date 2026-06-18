def is_odd_or_even(number: int) -> str:
    """
    Determines if a given integer is odd or even using the modulo operator.

    Args:
        number (int): The integer to check.

    Returns:
        str: A string indicating whether the number is 'odd' or 'even'.
    """
    remainder = number % 2
    
    # If the remainder is 0, the number is even; otherwise, it's odd.
    if remainder == 0:
        return "The number is even."
    else:
        return "The number is odd."

if __name__ == '__main__':
    sample_numbers = [3, 4, -5, 10]

    for num in sample_numbers:
        result = is_odd_or_even(num)
        print(f"{num}: {result}")