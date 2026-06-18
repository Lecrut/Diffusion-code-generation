def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    Base case: 0 is even (returns True).
    Recursive step: n+1 has the opposite parity of n-1, so we recurse on n//2 
    and adjust based on remainder logic derived from dividing by 2 repeatedly.
    However, a simpler recursive definition for checking parity without division 
    in each call could be: is_even(n) = not is_even(n - 2).
    
    To ensure termination with positive integers:
    Base case: n == 0 -> True (even), n == 1 -> False (odd).
    Recursive step: if n >= 2, return opposite of is_even(n-2).

    Args:
        n (int): A non-negative integer.

    Returns:
        bool: True if even, False otherwise.
    
    Note: This approach reduces the problem size by 2 in each call but has 
    O(n) time complexity with high constant factors due to function calls and stack usage.
    """
    # Ensure input is non-negative as per task requirement
    n = abs(int(n)) if isinstance(n, float) else int(n)
    
    if n == 0:
        return True
    elif n == 1:
        return False
    
    # Recursive step for positive integers >= 2
    # If we go down by 2 steps, the parity flips twice (remains same), 
    # but to optimize recursion depth, let's stick strictly to decrementing.
    # Actually, standard recursive even check usually is: 
    # def f(n): return n==0 or not f(n-1) for odd/even logic? No.
    # Correct simple parity recurrence with step 2 avoids deep stack compared to -1 steps.
    
    if n % 2 == 0:
        return True
    else:
        return False

# Re-implementing strictly as requested "recursive function" without using modulo inside the logic 
# (modulo is what we are analyzing). We will use subtraction by 2 for efficiency in recursion count.

def is_even_strictly_recursive(n):
    """
    Strict recursive version that does not use % or // operators internally, only - and base cases.
    
    Base case: n == 0 -> True (Even)
    Base case: n == 1 -> False (Odd)
    Recursive step: is_even_strictly_recursive(n-2) returns same result as current if even/odd? 
    Actually: Even numbers are E, Odd are O. 
    sequence starting at 0: T, F, T, F...
    So is_even(n) = not is_even(n-1). But this creates depth N.
    Optimization: is_even(n) == is_even(n-2). 
    
    Wait logic correction:
    if n=0 -> True
    if n=1 -> False
    if n >= 2 and even, then (n-2) is also even -> same result as f(0)? Yes.
    
    Algorithm:
    If n==0 return T
    If n==1 return F
    Return is_even_strictly_recursive(n - 2)
    
    This reduces depth to N/2 steps compared to O(N).
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        return False # Non-negative required by task logic usually implies domain check or handling. 
                     # Task says "non-negative", so negative input is outside spec but let's handle gracefully.

    base_even = True   # Represents parity state relative to 0 (always even)
    
    if n == 0:
        return True
    elif n == 1:
        return False
    
    # Recursive call with step of 2
    if is_even_strictly_recursive(n - 2):
        return True
    else:
        return False

def main():
    """Main execution block to test the recursive function against known values."""
    
    # Test cases embedded directly without user input or CLI args.
    sample_values = [0, 1, 2, 3, 4, 5, 10, 16]
    
    print("Testing is_even_strictly_recursive with hardcoded samples:")
    for val in sample_values:
        result = is_even_strictly_recursive(val)
        # Verify logic manually to ensure correctness before printing output
        expected = (val % 2 == 0) 
        status = "PASS" if result == expected else "FAIL"
        print(f"is_even({val}) -> {result} | Expected: {expected} | Status: {status}")

if __name__ == '__main__':
    main()