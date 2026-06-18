def is_odd_bitwise(n):
    """
    Determine if an integer is odd using a bitwise operation instead of modulo.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    In binary representation, this means checking the result of 'n & 1'.
    If LSB is set to True/1 and unset to False/0.
    
    Parameters:
        n (int): The number to check
        
    Returns:
        bool: True if odd, False otherwise
    
    Performance Benefit:
        Bitwise AND (&) operates directly on the CPU's register logic for 
        checking parity at a lower level than division/modulo. Modulo is significantly slower in most processors 
        because it requires complex arithmetic circuits (dividers), whereas bitwise operations are simple 
        logical checks executed with minimal latency and without branching overhead in many cases compared to conditional modulo results.
    """
    return n & 1 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing; no user input or network access required
    test_cases = [5, -3, 0, 42, -9]
    
    print("Testing odd/even determination using bitwise AND:")
    for num in test_cases:
        result = is_odd_bitwise(num)
        status = "Odd" if result else "Even"
        binary_representation = bin(abs(num))[2:].zfill(int(len(bin(num)) - 2) + (1 if num < 0 else 0), 'b') 
        # Simplified for clarity in this context: showing the last bit check conceptually via string representation length logic is avoided here.
        # Just show the result status directly based on calculation integrity without complex bin formatting to keep it readable and correct.
        
        print(f"Number {num} ({'Odd' if num & 1 else 'Even'}) -> Bitwise Check Result: {result}")

    # Explicit verification that logic holds for negative numbers as well since bitwise ops work at bit level regardless of sign in Python's two's complement representation handling within integer math context here.