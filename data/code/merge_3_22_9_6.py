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
    test_values = [0, 1, -2, -3, 456789]
    
    print("Testing odd/even determination using bitwise AND:")
    for val in test_values:
        result = is_odd_bitwise(val)
        status = "Odd" if result else "Even"
        print(f"{val} -> {status}")

# Performance Explanation (for context, not part of the executable output):
# The modulo operator (%) involves division logic which can be computationally expensive 
# especially for large numbers or in tight loops. Bitwise AND (&) operates directly on bits,
# making it significantly faster and more efficient at the CPU level. It avoids arithmetic overhead.