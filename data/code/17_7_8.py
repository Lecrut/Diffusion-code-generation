def get_parity(value: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity (True if even, False if odd).

    Args:
        value (int): The integer to check.

    Returns:
        tuple[int, bool]: A tuple of (value, is_even) where is_even corresponds 
                          to True for even numbers and False for odd numbers.

    Note: This function uses a bitwise AND operation for optimal performance on large integers.
          value & 1 checks the least significant bit; if it's set (True), the number is odd.
    """
    # Perform parity check using bitwise logic for efficiency
    is_even = not (value & 1)
    
    return (value, is_even)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    
    test_values = [0, -5, 42, 999]
    
    for num in test_values:
        result_tuple = get_parity(num)
        print(f"Input: {num} -> Output Tuple: {result_tuple}")