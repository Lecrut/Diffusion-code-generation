def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    This can be checked by performing a bitwise AND with 1.
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if n is odd, False otherwise
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments
    test_values = [0, 1, -3, 42, -5]
    
    print("Testing odd determination using bitwise AND:")
    for val in test_values:
        result = is_odd_bitwise(val)
        # Verify correctness against modulo operator (for internal validation only)
        expected = val % 2 != 0 if val >= 0 else abs(val) % 2 != 0
        status = "PASS" if result == expected else "FAIL"
        print(f"{val}: {result} ({status})")

    # Demonstrate performance difference conceptually (not timing in this static context)
    sample_num = 1_073_741_829  # Large odd number
    
    bitwise_result = is_odd_bitwise(sample_num)
    
    print(f"\nSample large number: {sample_num}")
    print(f"Bitwise check (AND with 1): {bitwise_result}")