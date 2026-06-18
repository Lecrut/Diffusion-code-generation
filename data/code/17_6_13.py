def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    Base case: 0 is even.
    Recursive step: n-1 has the opposite parity of n.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        bool: True if n is even, False otherwise
    """
    # Handle base cases for safety and clarity
    if n == 0:
        return True
    
    # Recursive step: decrement by 1 until reaching the next number with known parity
    # Since we start at an arbitrary non-negative integer, this will eventually hit 0 or 1
    # However, to optimize slightly within recursion depth limits for large numbers,
    # we can use a simpler logic: n is even if (n-2) was checked and returned True/False appropriately.
    # But strictly following the "determine" requirement via simple decrement:
    
    return not is_even_recursive(n - 1)

def is_even_modulo(n: int) -> bool:
    """
    Directly determine if a non-negative integer is even using modulo operator.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        bool: True if n is even, False otherwise
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test both functions without user input
    
    samples = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    print("Testing Recursive Approach:")
    for num in samples:
        result_rec = is_even_recursive(num)
        status = "Even" if result_rec else "Odd"
        print(f"{num}: {status}")
        
    print("\nTesting Modulo Approach:")
    for num in samples:
        result_mod = is_even_modulo(num)
        status = "Even" if result_mod else "Odd"
        print(f"{num}: {status}")
    
    # Verification that both approaches yield identical results
    all_match = True
    for num in samples:
        match = (is_even_recursive(num) == is_even_modulo(num))
        if not match:
            all_match = False
    
    print("\nVerification:")
    print(f"All test cases matched between recursive and modulo approaches: {all_match}")