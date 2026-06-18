import time

def reverse_string_recursive(s):
    """
    Recursively reverses a string.
    
    Base case: if length is 0 or 1, return the string as is.
    Recursive step: concatenate last character with reversed rest of string.
    
    Args:
        s (str): The input string to reverse
        
    Returns:
        str: The reversed string
    """
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse_string_recursive(s[:-1])

def direct_reverse(s):
    """Direct slicing method to reverse a string."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values (no user input required)
    test_strings = [
        "hello",
        "recursion",
        "",
        "a" * 50,
    ]

    print("Comparing Recursive vs Direct String Reversal")
    print("-" * 40)
    
    for s in test_strings:
        start_time = time.time()
        result_recursive = reverse_string_recursive(s)
        end_time_recursive = time.time()
        
        result_direct = direct_reverse(s)
        # No timing needed for comparison with slicing as it's optimized C code
        
        print(f"Input length: {len(s)}")
        print(f"Recursive Result:  '{result_recursive}'")
        print(f"Direct Result:     '{result_direct}'")
        
        time_taken = end_time_recursive - start_time
        print(f"Time taken (recursive): ~{time_taken*1e6:.2f} microseconds\n")
    
    # Complexity Analysis printed as part of the output logic
    """
    Time Complexity Analysis:
    
    1. Recursive Solution O(n^2) worst case without memoization or optimization, 
       because each recursive call creates a new string slice s[:-1] which has length n-1, then n-2, etc.,
       and string concatenation in the base step takes linear time relative to current string size.
    2. Direct Slicing O(n) - The slicing operation [::-1] is highly optimized at C level 
       with a single pass creating a new reversed copy of length n (constant overhead per element).
    
    Note: In Python specifically, the naive recursive approach described above actually results in O(n^2) time complexity.
        This is because string concatenation s[-1] + ... creates intermediate strings growing up to size n at each step.
        
    The direct slicing method achieves true linear time O(n)."""