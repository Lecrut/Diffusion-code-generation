def get_number_parity(number):
    """
    Returns a tuple containing the input number and its parity (True for even, False for odd).
    
    Args:
        number (int): The integer to check.
        
    Returns:
        Tuple[int, bool]: A tuple of (number, is_even) where is_even indicates if the number is even.
    """
    return (number, not number % 2)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    samples = [0, -5, 100, 42]
    
    for num in samples:
        result = get_number_parity(num)
        print(f"Input: {num}, Parity (even): {result[1]}")