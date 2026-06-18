def get_number_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input number and its parity (True if even, False if odd).
    
    Args:
        number (int): The integer to check.
        
    Returns:
        tuple[int, bool]: A tuple of (number, is_even) where is_even is True for even numbers.
    """
    return (number, not number % 2)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [0, -5, 42, 100]

    for num in samples:
        result = get_number_parity(num)
        print(f"Input: {num}, Parity (even): {result[1]}")