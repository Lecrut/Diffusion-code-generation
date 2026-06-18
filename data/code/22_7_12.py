def get_remainder(number):
    """
    Takes an integer and returns the remainder when divided by 2.
    
    Parameters:
        number (int): The integer to check
        
    Returns:
        int: Remainder of number // 2, used as parity indicator
            Even numbers return 0, Odd numbers return 1
            
    Example:
        >>> get_remainder(5)
        1
        >>> get_remainder(4)
        0
    """
    remainder = number % 2
    
    if remainder == 0:
        parity_name = "Even"
    else:
        parity_name = "Odd"
        
    return remainder, parity_name

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or file access
    test_cases = [1, 2, -3, 0]
    
    for num in test_cases:
        rem, status = get_remainder(num)
        print(f"Number {num}: Remainder={rem}, Parity is {status}")