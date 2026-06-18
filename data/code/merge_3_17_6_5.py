def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    # Base case: 0 is even
    if n == 0:
        return True
    # Recursive step: decrement by 1 and flip result of next call
    else:
        # If we reach negative numbers (should not happen with valid input), 
        # the logic still holds mathematically but may be inefficient.
        if n < 0:
            raise ValueError("Input must be non-negative.")
        
        return is_even_recursive(n - 1) ^ True

def is_even_direct(n: int) -> bool:
    """
    Directly determine if a non-negative integer is even using modulo operator.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments
    
    test_cases = [0, 1, 5342]
    
    print("Testing Recursive Approach:")
    for num in test_cases:
        result_rec = is_even_recursive(num)
        
    print("\nDirect Modulo Results (for comparison):")
    for num in test_cases:
        res_direct = is_even_direct(num)

    # Demonstrate the actual values of recursive calls to prove correctness and overhead conceptually
    sample_check = 10
    
    # Print results clearly showing that both methods yield identical boolean outcomes
    if __name__ == '__main__':
        final_test_num = 42
        
        print(f"\n--- Final Verification for {final_test_num} ---")
        
        rec_result = is_even_recursive(final_test_num)
        dir_result = is_even_direct(final_test_num)
        
        assert rec_result == dir_result, "Recursive and Direct results mismatch!"
        print(f"Is Even? (Recursive):   {rec_result}")
        print(f"Is Even? (Direct Mod):  {dir_result}")