def get_remainder_and_parity(number: int) -> tuple[int, str]:
    """
    Takes an integer and returns a tuple containing:
        1. The remainder of the number divided by 2 (0 or 1).
        2. A string indicating if the number is 'even' or 'odd'.

    Args:
        number (int): The integer to evaluate.

    Returns:
        tuple[int, str]: A tuple with the remainder and the parity description.
    """
    remainder = number % 2
    
    # Determine parity based on the remainder
    if remainder == 0:
        parity_description = "even"
    else:
        parity_description = "odd"

    return (remainder, parity_description)

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [10, 7, -3, 0]

    for num in samples:
        remainder, is_even_or_odd = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder mod 2: {remainder}, Parity: {is_even_or_odd}")