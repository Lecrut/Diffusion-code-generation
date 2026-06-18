def get_number_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple (number, is_even).
    
    Args:
        number (int): The input integer.
        
    Returns:
        tuple[int, bool]: A tuple containing the original number and 
                          True if it is even, False otherwise.
                          
    Performance Note: Uses bitwise AND (&) with 1 for O(1) time complexity
    instead of modulo operator (%) which involves division logic internally.
    """
    return (number, not (number & 1))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [0, -5, 42, 999]
    
    for value in test_cases:
        result_tuple = get_number_parity(value)
        print(f"Input: {value}, Parity (is even): {result_tuple[1]}")