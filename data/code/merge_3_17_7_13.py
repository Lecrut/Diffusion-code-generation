def get_parity_and_value(number):
    """
    Returns a tuple containing the input number and its parity as booleans.
    
    Args:
        number (int): The integer to process.
        
    Returns:
        Tuple[int, bool]: A tuple where the first element is the original number 
                          and the second indicates if it is even or odd.
                          
    Performance Note: Uses bitwise AND (& 1) for O(1) parity check instead of modulo operator.
    """
    return (number, not bool(number & 1))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without input or network access
    test_cases = [0, -5, 42, -3, 1]
    
    for case in test_cases:
        result = get_parity_and_value(case)
        print(f"Input: {case}, Parity (Even): {result[1]}, Output Tuple: {result}")