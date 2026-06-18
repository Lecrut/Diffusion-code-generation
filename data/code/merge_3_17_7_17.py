def get_number_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity status.
    
    Args:
        number (int): The integer to check
        
    Returns:
        tuple[int, bool]: A tuple of (number, is_even) where is_even is True if even, False otherwise
    """
    return (number, number % 2 == 0)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [10, -3, 42, 0, 7]
    
    for num in samples:
        result = get_number_parity(num)
        print(f"Input: {num}, Parity (even): {result[1]}")