def is_odd_bitwise(n: int) -> bool:
    """
    Determines if an integer is odd using a bitwise operation instead of modulo.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    This can be checked by performing a bitwise AND with 1.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    test_values = [0, 1, -5, 42, -3]

    print("Testing oddness using bitwise operations:")
    for val in test_values:
        result = is_odd_bitwise(val)
        expected = val % 2 != 0 if val >= 0 else abs(val) % 2 != 0
        status = "PASS" if result == expected else "FAIL"
        print(f"{val}: Bitwise Result={result}, Expected={expected} -> {status}")

    # Performance explanation comment:
    # The bitwise AND operation (n & 1) is generally faster than the modulo operator (%) 
    # because it involves a simple CPU instruction that checks the least significant bit,
    # whereas division/modulo often requires more complex arithmetic operations.