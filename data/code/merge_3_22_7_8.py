def get_remainder_and_parity(number: int) -> tuple[int, str]:
    """
    Takes an integer and returns a tuple containing its remainder when divided by 2
    and whether it is odd or even based on that parity.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        tuple[int, str]: A tuple where the first element is the remainder 
                        (0 for even, 1 for odd) and the second element is a string 
                        describing the parity ("even" or "odd").
    """
    # Calculate remainder when divided by 2 using modulo operator
    remainder = number % 2
    
    # Determine if the number is even or odd based on the remainder
    if remainder == 0:
        parity_description = "even"
    else:
        parity_description = "odd"
    
    return remainder, parity_description

if __name__ == '__main__':
    sample_numbers = [10, -5, 3]
    
    for num in sample_numbers:
        rem, desc = get_remainder_and_parity(num)
        print(f"Number {num}: Remainder is {rem}, Parity is {desc}")