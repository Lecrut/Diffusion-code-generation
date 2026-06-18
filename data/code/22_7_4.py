def get_remainder_and_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the remainder of number divided by 2 
    and whether the number is odd (True) or even (False).
    
    Args:
        number (int): The integer to check.
        
    Returns:
        tuple[int, bool]: A tuple where the first element is the remainder 
                          modulo 2, and the second element indicates if the number 
                          is odd (True) or even (False).
    """
    remainder = number % 2
    is_odd = remainder == 1
    
    return remainder, is_odd

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    samples = [4, 7, -3, 0]

    for num in samples:
        rem, odd_status = get_remainder_and_parity(num)
        
        if is_odd := (rem == 1):
            print(f"The number {num} has a remainder of {rem}. It is ODD.")
        else:
            print(f"The number {num} has a remainder of {rem}. It is EVEN.")