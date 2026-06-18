def is_even_recursive(n):
    """
    Recursively determine if a non-negative integer is even.
    
    Args:
        n (int): A non-negative integer to check
        
    Returns:
        bool: True if n is even, False otherwise
    
    Raises:
        ValueError: If n is negative
    """
    # Base case for recursion limit and validity checking
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Recursive step: decrement by 1 until we reach the base cases (0 or 1)
    if n == 0:
        return True
    
    elif n == 1:
        return False
        
    else:
        # Continue recursion with n - 2 to optimize parity checking steps, 
        # though standard decrement by 1 is logically equivalent.
        return is_even_recursive(n - 2)

def check_modulo_oddity(n):
    """Wrapper for direct modulo approach"""
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return n % 2 == 1

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    samples = [0, 1, 2, 3, 4, 5, 10, 99]
    
    print("Testing is_even_recursive:")
    for num in samples:
        result_recursion = is_even_recursive(num)
        
        # Calculate expected result using modulo arithmetic logic directly 
        # to demonstrate the comparison point. Note that check_modulo_oddity returns True if odd, False if even.
        expected_result_is_even = (num % 2 == 0)
        
        status = "PASS" if result_recursion else "FAIL"
        
        print(f"is_even_recursive({num}) -> {result_recursion}") 
        print(f"\tDirect Modulo Check: Expected Even? {expected_result_is_even} | Status: {status}\n")