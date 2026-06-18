def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    A number n is even or divisible by 2 iff (n & 1) == 0, because 
    the least significant bit represents whether the number is odd or not.
    If any other bits are set, they do not affect divisibility by 2 for integers;
    thus checking only LSB provides an optimized check without modulo overhead.
    
    Args:
        n (int): The integer to evaluate
        
    Returns:
        bool: True if the number is odd, False otherwise
    """
    return bool(n & 1)

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    test_cases = [-5, -4, 0, 3, 7, 89]
    
    print("Testing is_odd_bitwise function:")
    all_passed = True
    
    for num in test_cases:
        result = is_odd_bitwise(num)
        expected = num % 2 != 0
        
        if result == expected:
            status_str = "PASS"
        else:
            status_str = "FAIL"
            all_passed = False
            
        print(f"is_odd({num}) => {result} (Expected: {expected}), Status: {status_str}")
    
    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed.")