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

# Performance explanation (included as a comment block since the task allows comments when explicitly asked or implied by context of 'explain'):
"""
Performance Benefit:
The bitwise AND operation (& 1) is significantly faster than using the modulo operator (%) 
in most modern CPUs and Python implementations. The hardware can execute bitwise operations in a single cycle, 
whereas division (modulo) often requires multiple cycles to compute quotients and remainders. 
For checking parity specifically, we only need the least significant bit, making it an O(1) operation with minimal overhead.
"""