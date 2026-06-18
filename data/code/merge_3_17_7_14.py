def get_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        Tuple[int, bool]: A tuple where the first element is the original 
                          number and the second indicates if it's even (True) or odd (False).
                          
    Performance Note: Uses bitwise AND with 1 for O(1) time complexity per operation.
    """
    return (number, not (number & 1))

if __name__ == '__main__':
    # Hard-coded sample values that run without user input or external dependencies
    samples = [0, -5, 42, 1]
    
    for num in samples:
        result = get_parity(num)
        print(f"Input: {num}, Parity (Even): {result[1]}")