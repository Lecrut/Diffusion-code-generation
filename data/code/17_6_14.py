def is_even_recursive(n):
    """
    Recursively determines if a non-negative integer is even.
    
    Logic: 
    - Base case: 0 is even (True).
    - Recursive step: n-1 has the opposite parity of n, so we flip the result recursively until reaching base cases or negative numbers (though input should be non-negative per task spec).
      However, a simpler recursive definition for "is_even" could be:
        is_even(n) = not is_even(n - 2) with base case is_even(0)=True.
    But to strictly follow recursion depth without skipping by 2 (which might look like iteration), 
    we can do the standard decrement approach which flips parity each step, but that's inefficient for large n due to stack depth and operations.
    
    Let's use a cleaner recursive definition:
      is_even(0) -> True
      is_even(n) = not is_even(n - 1) if n > 0
    
    This works correctly but uses O(n) time complexity per call, unlike the modulo approach which is O(1).
    
    Parameters:
        n (int): A non-negative integer.
        
    Returns:
        bool: True if even, False otherwise.
    """
    # Base case for recursion
    if n == 0:
        return True
    
    # Recursive step: decrement by 1 and invert the result of the previous check
    return not is_even_recursive(n - 1)

def is_even_modulo(n):
    """
    Directly determines if a non-negative integer is even using modulo.
    
    Parameters:
        n (int): A non-negative integer.
        
    Returns:
        bool: True if even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [0, 1, 2, 3, 4, 5, 100, 99]
    
    print("Testing Recursive Approach:")
    for num in test_cases:
        result_rec = is_even_recursive(num)
        
    # Note: Printing all results at once to avoid excessive output lines if desired, 
    # but here we iterate and store or print directly. Since the task doesn't specify format rigorously beyond runnable module,
    # let's print them clearly.
    
    for num in test_cases:
        res = is_even_recursive(num)
        mod_res = is_even_modulo(num)
        
        status = "MATCH" if res == mod_res else "MISMATCH (ERROR)"
        print(f"{num}: Recursive={res}, Modulo={mod_res} -> {status}")

    # Additional critique note embedded in logic verification:
    # The recursive approach has O(n) time complexity and O(n) space complexity due to call stack.
    # The modulo approach is O(1) time and O(1) space.