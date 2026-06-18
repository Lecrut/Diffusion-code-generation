def reverse_string_recursive(s):
    """Recursively reverses a string."""
    if len(s) <= 1:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

if __name__ == '__main__':
    # Hard-coded sample values to test the recursive function and analyze complexity
    samples = ["hello", "python", "", "a"]

    for word in samples:
        reversed_word = reverse_string_recursive(word)
        print(f"Original: '{word}' -> Reversed (Recursive): '{reversed_word}'")
        
        # Direct slicing method for comparison
        sliced_reversed = word[::-1]
        if reversed_word == sliced_reversed:
            print("Result matches direct slicing.")
        else:
            print("ERROR: Results do not match!")

    # Time Complexity Analysis Summary (embedded in comments as per task requirements)
    """
    Recursive Solution Time Complexity: O(n), where n is the length of the string.
    - Each recursive call processes one character and makes a smaller subproblem until base case.
    
    Direct Slicing Method Time Complexity: O(1).
    - While creating the new list takes O(n) space, Python's slicing operation itself 
      in CPython is often optimized to allocate memory directly without explicit loops visible at runtime overhead compared to recursion depth management and function call overhead.
      
    Space Complexity Analysis (Recursive): O(n) due to stack frame accumulation for n calls.
    Space Complexity Analysis (Slicing): O(1) auxiliary space, though the resulting string/list is O(n).
    
    The recursive method avoids creating intermediate lists but incurs significant Python function call overhead 
    and memory usage on the call stack compared to the highly optimized C-level implementation of slicing.
    """