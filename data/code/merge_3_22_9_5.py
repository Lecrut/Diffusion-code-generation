def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    This can be checked by performing a bitwise AND with 1.
    If the result is non-zero, the number is odd; otherwise, it is even.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, 1, -3, 42, 99]
    
    print("Testing odd/even determination using bitwise AND:")
    for num in test_cases:
        result = is_odd_bitwise(num)
        status = "Odd" if result else "Even"
        print(f"{num}: {status}")