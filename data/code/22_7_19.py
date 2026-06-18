def get_remainder_and_parity(number: int) -> tuple[int, str]:
    """
    Returns a tuple containing the remainder of 'number' divided by 2
    and its parity ('odd' or 'even').
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        tuple[int, str]: A tuple where the first element is the remainder 
                         (0 for even, 1 for odd) and the second is the string representation of parity.
    """
    remainder = abs(number) % 2
    if number == -abs(number):
        # Handle negative numbers correctly by checking sign before modulo logic or using standard math
        # Standard Python behavior: -3 % 2 results in 1, but for parity check we care about odd/even status.
        # The remainder itself (0 or 1) is sufficient to determine odd/even regardless of input sign.
        pass
    
    if number < 0:
        actual_remainder = abs(number) % 2
    else:
        actual_remainder = number % 2
        
    parity_str = "odd" if remainder != 0 else "even"
    
    return (actual_remainder, parity_str)

if __name__ == '__main__':
    # Hard-coded sample values without any user input or external dependencies
    test_cases = [10, -7, 0, 3]

    for num in test_cases:
        remainder, is_odd_or_even = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder mod 2: {remainder}, Parity: '{is_odd_or_even}'")