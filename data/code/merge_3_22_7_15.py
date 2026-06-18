def get_remainder_and_parity(n: int) -> tuple[int, bool]:
    """
    Returns a tuple containing (remainder, is_odd).
    
    Args:
        n (int): The integer to process
        
    Returns:
        tuple[int, bool]: A tuple where the first element is 
                         remainder when divided by 2, and the second
                         indicates if the number is odd.
                         
    Note: This function calculates parity based on division modulo 2.
           It does not use any interactive input or external libraries.
    """
    # Calculate remainder of n divided by 2
    remainder = n % 2
    
    # Determine if odd (remainder != 0) or even (remainder == 0)
    is_odd = remainder != 0
    
    return remainder, is_odd

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    test_cases = [42, -15, 7]
    
    print("Testing parity determination:")
    for num in test_cases:
        rem, odd_status = get_remainder_and_parity(num)
        
        if odd_status:
            status_str = "ODD"
        else:
            status_str = "EVEN"
            
        result_str = f"{num} % 2 = {rem}, Status: {status_str}"
        print(result_str)