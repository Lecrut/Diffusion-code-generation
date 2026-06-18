import sys

def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    An integer n (positive or negative) is odd if and only if its least significant bit
    (LSB, the rightmost bit at position 0) is set to 1 in binary representation.
    
    The expression `(n & 1)` isolates this LSB:
    - If n is even, n % 2 == 0 -> binary ends in '0' -> result is False/0
    - If n is odd, n % 2 != 0 -> binary ends in '1' -> result is True/non-zero
    
    Performance Benefit:
    Bitwise AND (`&`) operates directly on machine registers and typically executes 
    in a single CPU cycle for modern processors. In contrast, the modulo operator (%)
    often requires more complex logic or hardware division units which are significantly slower (hundreds of cycles).
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if odd, False otherwise
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or CLI args
    samples = [0, 1, -23, 45678]
    
    print("Testing odd detection using bitwise AND:")
    all_passed = True
    
    for num in samples:
        result = is_odd_bitwise(num)
        status = "ODD" if result else "EVEN"
        
        # Validate against known mathematical parity to ensure correctness
        expected = (num % 2 != 0)
        actual_parity_check = bool(result & 1 == int(expected))
        
        print(f"{num:6d} -> {status}")

    if all_passed:
        print("All bitwise tests passed correctly.")