def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    
    This function uses a bitwise AND operation to check the least significant bit,
    which is generally more efficient than using the modulo operator for large integers.
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if n is even, False otherwise
    """
    return n & 1 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -5, 42, -8, 999]
    
    results = []
    for val in test_values:
        result = is_even(val)
        results.append((val, result))
        
    # Print results to verify correctness (no interactive prompts used)
    print("Testing is_even function:")
    for num, expected in results:
        status = "PASS" if expected else "FAIL"
        print(f"is_even({num}) -> {result} | Expected: True/False ({status})")