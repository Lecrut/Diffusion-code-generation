def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    Base case: 0 is even.
    Recursive step: n-1 has the opposite parity of n, so we recurse until reaching 0 or -1 (though input guarantees non-negative).
    Note: This approach will eventually hit negative numbers if not carefully bounded for odd inputs > max_int, 
           but logically it flips state on each decrement. For safety with large integers and recursion limits,
           this is primarily a demonstration of the concept rather than production code for very large n.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if even, False otherwise.
    """
    # Base case: 0 is even
    if n == 0:
        return True
    
    # Recursive step: decrement by 1 and negate the result of the previous call
    # This works because parity flips with every subtraction from an odd number to reach zero (odd steps -> False), 
    # or even number to reach zero (even steps -> True). However, strictly speaking, n-1 has opposite parity.
    return not is_even_recursive(n - 1)

def is_even_modulo(n: int) -> bool:
    """
    Directly determine if a non-negative integer is even using modulo operator.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [0, 1, 2, 3, 4, 5, 100]
    
    print("Testing Recursive Approach:")
    for num in test_cases:
        result_rec = is_even_recursive(num)
        
    print("\nTesting Modulo Approach:")
    for num in test_cases:
        res_mod = is_even_modulo(num)

    # Verification block to ensure both methods yield identical results on samples
    all_match = True
    for n in test_cases:
        if not (is_even_recursive(n) == is_even_modulo(n)):
            print(f"Mismatch at {n}: Recursive={is_even_recursive(n)}, Modulo={is_even_modulo(n)}")
            all_match = False
            
    if all_match:
        print("All sample tests passed. Both methods agree.")