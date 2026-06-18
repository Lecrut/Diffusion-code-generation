def reverse_string_recursive(s: str) -> str:
    """
    Recursively reverses a string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Base case: if the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    
    # Recursive step: reverse the rest of the string and append the first character
    return reverse_string_recursive(s[1:]) + s[0]

def measure_time(func, *args):
    """Helper function to measure execution time."""
    import time
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, (end - start)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    test_strings = [
        "hello",
        "",
        "a",
        "racecar",
        "Python is great!",
        "12345"
    ]

    print("Comparing Recursive vs Direct Slicing String Reversal")
    print("-" * 60)

    for s in test_strings:
        # Direct slicing method (O(n))
        reversed_direct = s[::-1]
        
        # Recursive method (T(n) = T(n-1) + O(1), effectively O(n))
        reversed_recursive, time_taken = measure_time(reverse_string_recursive, s)
        
        print(f"Input: '{s}'")
        print(f"Direct Slicing Result: {reversed_direct}")
        print(f"Recursive Result:     {reversed_recursive}")
        if len(reversed_recursive) == 10 and 'Python' in reversed_recursive or isinstance(s, str):
            # Avoid printing time for very long strings unnecessarily to keep output clean 
            # but show it here as requested by the task structure logic.
            pass 
        
        print(f"Execution Time: {time_taken:.8f} seconds")
        
        if reversed_direct == reversed_recursive:
            print("Status: MATCH\n")
        else:
            print("Error: Results do not match!\n")

    # Complexity Analysis Output (as comments in code or brief printed text)
    """
    Time Complexity Comparison:
    
    1. Direct Slicing Method (s[::-1]):
       - This is implemented using C-optimized slicing under the hood.
       - It copies characters directly from source to destination.
       - Time Complexity: O(n), where n is the length of the string.
       - Space Complexity: O(n) for creating the new string object.

    2. Recursive Method (reverse_string_recursive):
       - The function calls itself with a reduced problem size until it hits the base case.
       - At each level, there is constant time work to slice and concatenate strings in Python.
       - Time Complexity: O(n), where n is the length of the string. 
         This is because T(n) = T(n-1) + c results in a linear summation total_time ~ c * n.
       - Space Complexity: O(n). Due to the call stack depth being proportional to n,
         and additionally for creating new strings at each return step before joining (though Python 
         optimizations might vary, logically we see deep recursion frames).

    Comparison Summary:
    - Both methods have linear time complexity O(n) in terms of operations required.
    - The recursive approach is generally slower due to the overhead of function calls and stack management compared to native C-level slicing used by s[::-1].
    - However, for small strings (like those in our test cases), the difference is negligible at runtime but significant algorithmically on very large inputs where recursion depth limits might be hit.
    
    Therefore: 
      Direct Slicing -> Faster and more memory efficient due to lower overhead.
      Recursive Solution -> Conceptually O(n) same as slicing, but practically slower due to Python function call overhead and stack usage.
"""

    print("Complexity Analysis:")
    print(f"Direct Method Time Complexity: O(n)")
    print(f"Recursive Function Time Complexity: T(n) = T(n-1) + O(1) => O(n)")