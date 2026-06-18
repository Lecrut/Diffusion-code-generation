def get_remainder_and_parity(n: int) -> tuple[int, str]:
    """
    Returns a tuple containing the remainder of n divided by 2
    and whether n is 'odd' or 'even'.
    
    Args:
        n (int): The integer to process.
        
    Returns:
        tuple[int, str]: A tuple where index 0 is the remainder 
                         and index 1 is the string representation of parity.
    """
    remainder = n % 2
    
    if remainder == 0:
        return remainder, "even"
    else:
        return remainder, "odd"

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    samples = [10, 7, -3, 0]
    
    for num in samples:
        rem, parity = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder mod 2: {rem}, Parity: {parity}")