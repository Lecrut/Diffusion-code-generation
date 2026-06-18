def get_number_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity status.
    
    The parity is True if the number is even, False otherwise (odd).
    
    Args:
        number (int): The integer to check for parity.
        
    Returns:
        tuple[int, bool]: A tuple of (the original number, is_even boolean).
    """
    return (number, number % 2 == 0)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [10, -3, 42, 0, 7]

    for sample in samples:
        result_number, is_even = get_number_parity(sample)
        print(f"Input: {sample}")
        print(f"Parsed Tuple: ({result_number}, {is_even})")