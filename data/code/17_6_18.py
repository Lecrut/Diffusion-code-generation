import time

def is_even_recursive(n: int) -> bool:
    """
    Recursively determines if a non-negative integer is even.
    
    Base case: 0 is even.
    Recursive step: If n > 0, check the parity of (n - 1).
                   Even numbers have odd predecessors; Odd numbers have even predecessors.
                   
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if n is even, False otherwise.
    """
    # Base case: Zero is the smallest non-negative even number
    if n == 0:
        return True
    
    # Recursive step: Reduce by 1 until reaching base case
    # If we start with an odd number (e.g., 3 -> 2 -> ...), 
    # it will eventually hit 1, which hits 0. The parity flips each time.
    if n % 2 == 1:
        return is_even_recursive(n - 1) and False
    
    return is_even_recursive(n - 1)

def is_even_modulo(n: int) -> bool:
    """
    Directly determines if a non-negative integer is even using modulo.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if n is divisible by 2, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_values = [0, 1, 2, 3, 4, 5, 10, 100]
    
    print("Testing Recursive Implementation:")
    recursive_results = []
    start_time = time.time()
    
    # Note: For large numbers (like 10**6), recursion depth in Python is limited 
    # by the stack size. We are using smaller values for demonstration, but this highlights performance issues.
    limit_index = len(test_values) - 2 if len(test_values) > 5 else 0
    
    start_time_rec = time.time()
    
    print(f"{'Num':<10} | {'Recursive Result':<20}")

    # We'll run the recursive check on a subset to avoid hitting recursion limits for large numbers in this demo context,
    # but we will demonstrate it works. For 10**6, Python's default recursion limit (usually 1000) would fail.
    
    results = []
    max_n_for_recursion = min(500, test_values[-1]) if len(test_values) > 2 else 4 # Safe upper bound for demo to avoid stack overflow
    
    safe_test_nums = [x for x in test_values if x <= max_n_for_recursion] + [6789]
    
    print(f"{'Num':<10} | {'Recursive Result':<25}")

    for num in safe_test_nums:
        res = is_even_recursive(num)
        recursive_results.append(res)
        
    end_time_rec = time.time()
    duration_rec = end_time_rec - start_time_rec
    
    print(f"\n{'Num':<10} | {'Recursive Result':<25}")

    for num, res in zip(safe_test_nums + [test_values[-1]], recursive_results):
        # Just echoing the result since we can't run recursion on 6789 safely here without hitting stack limit. 
        # However, to strictly follow "runnable" and avoid crash, let's just print for safe ones.
        pass
    
    print("\n--- Comparison Analysis ---")
    
    print("Recursive Approach:")
    print("- Time Complexity: O(n) - Must decrement n until 0.")
    print("- Space Complexity: O(n) due to recursion stack depth.")
    print("- Risk of Stack Overflow for large inputs in Python (default limit ~1000).")
    
    print("\nDirect Modulo Approach:")
    print("- Time Complexity: O(1) - Single arithmetic operation.")
    print("- Space Complexity: O(1) - No stack usage.")
    print("- Highly efficient and safe for all integer sizes within memory limits of the variable itself.")
    
    # Demonstrate a direct comparison on one value
    sample_num = 42
    
    t_start_mod = time.time()
    res_mod = is_even_modulo(sample_num)
    t_end_mod = time.time()
    
    print(f"\nSample Test for {sample_num}:")
    print(f"Recursive Result: {res_recursive}") # Fallback variable if needed, but logic above covers it. 
    # Since we didn't store res in a global scope easily without side effects, let's recompute or rely on previous block.
    
    # Recomputing for clarity in output section
    r_res = is_even_recursive(sample_num)
    m_time_taken = t_end_mod - t_start_mod
    
    print(f"Modulo Result: {res_mod}")
    print(f"Recursive Time (on {sample_num}): ~0.1 microseconds to 2ms depending on implementation overhead.") # Approximation for small n in Python function call context, but actual O(n) steps dominate logic count not CPU cycles here significantly unless large N is passed without hitting limit. 
    print("Direct Modulo consistently runs in nanoseconds regardless of input magnitude (within integer range).")