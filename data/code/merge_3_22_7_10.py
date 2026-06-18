def get_remainder_and_parity(number: int) -> tuple[int, str]:
    """
    Returns a tuple containing the remainder of number divided by 2
    and whether the number is 'odd' or 'even'.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        tuple[int, str]: A tuple where index 0 is the remainder 
                         and index 1 is the parity string ('odd' or 'even').
    """
    remainder = number % 2
    
    if remainder == 1:
        return (remainder, "odd")
    else:
        return (remainder, "even")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [0, 3, -5, 42]

    for num in samples:
        remainder, parity = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder mod 2: {remainder}, Parity: {parity}")