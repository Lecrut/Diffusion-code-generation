def get_number_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity status.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        tuple[int, bool]: A tuple where the first element is the original 
                          number and the second is True if even, False otherwise.
                          
    Performance Note: Uses bitwise AND for O(1) parity checking instead of modulo operator.
    """
    return (number, not (number & 1))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    samples = [0, -5, 42, 999]
    
    for num in samples:
        result_num, is_even = get_number_parity(num)
        print(f"Number: {result_num}, Parity (Even): {is_even}")