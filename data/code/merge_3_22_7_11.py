def get_remainder_and_parity(number: int) -> tuple[int, str]:
    """
    Returns a tuple containing the remainder of number divided by 2
    and whether the number is 'odd' or 'even'.
    
    Args:
        number (int): The integer to process.
        
    Returns:
        tuple[int, str]: A tuple where the first element is the remainder 
                         (0 for even, 1 for odd) and the second is a string 
                         indicating parity ('odd' or 'even').
    """
    remainder = number % 2
    
    if remainder == 0:
        return remainder, "even"
    else:
        return remainder, "odd"

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [10, 7, -3, 0]

    for num in samples:
        rem, parity = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder mod 2: {rem}, Parity: {parity}")