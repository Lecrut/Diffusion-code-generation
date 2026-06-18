def get_parity(n: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity (True if even, False if odd).
    
    Args:
        n (int): The integer to check.
        
    Returns:
        tuple[int, bool]: A tuple of (n, is_even) where is_even is True for even numbers.
    """
    return n, n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [10, -3, 42, 0, 7]
    
    for num in samples:
        result = get_parity(num)
        print(f"Number: {result[0]}, Parity (Even): {result[1]}")