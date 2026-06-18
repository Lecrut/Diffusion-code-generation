def get_remainder_and_parity(number: int) -> tuple[int, str]:
    """
    Calculates the remainder of a number divided by 2 and determines its parity.
    
    Args:
        number (int): The integer to check
        
    Returns:
        tuple: A tuple containing the remainder (0 or 1) and the parity string ('even' or 'odd')
    """
    remainder = number % 2
    
    if remainder == 0:
        return remainder, "even"
    else:
        return remainder, "odd"

if __name__ == '__main__':
    # Hard-coded sample values to test the function
    test_cases = [10, 7, -3, 42]
    
    for num in test_cases:
        rem, parity = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder mod 2: {rem}, Parity: {parity}")