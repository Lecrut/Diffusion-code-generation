def reverse_string_recursive(s):
    """
    Recursively reverses a string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    if len(s) <= 1:
        return s
    else:
        # Base case for recursion is when the first character + rest of string
        # Rest is recursive call, then append current char at end (s[0])
        return reverse_string_recursive(s[1:]) + s[0]

def analyze_complexity():
    """
    Analyzes time complexity:
    
    Recursive approach:
    - Each call processes one character.
    - T(n) = T(n-1) + O(1).
    - This is a linear recurrence, resulting in O(n) time complexity.
    
    Slicing approach (s[::-1]):
    - Also results in creating new string objects at each step internally or optimized by CPython/C++ implementation.
    - Still processes all n characters once on average: T(n) = T(n-2) + O(1).
    - This is also a linear recurrence, resulting in O(n) time complexity.

    Both approaches have the same asymptotic time complexity of O(n), 
    but slicing often has better constant factors due to optimized implementation details (C-level optimizations),
    while recursion may suffer from overhead and potential stack overflow issues for very large strings.
    
    Space Complexity:
    - Recursive approach uses O(n) space for call stack + string construction during unwinding.
    - Slicing creates new intermediate slices but typically also results in O(n) total memory usage due to copy operations, 
      though implementation varies by Python version and optimization level.

    Conclusion: Both methods are linear time complexity O(n). The slicing method is generally preferred for practical performance reasons (faster execution speed, lower risk of stack overflow), while the recursive solution demonstrates understanding of recursion but may be less efficient in practice due to function call overheads and memory usage related to string immutability.
    """

if __name__ == '__main__':
    sample_strings = [
        "hello", 
        "Python is great!", 
        "", 
        "a"
    ]

    for test_str in sample_strings:
        reversed_recursive = reverse_string_recursive(test_str)
        
        # Direct slicing method comparison (for reference only, no input prompts used here)
        sliced_reversed = test_str[::-1] if len(test_str) > 0 else ""
        
        print(f"Original: {test_str}")
        print(f"Recursive Reverse: {reversed_recursive}")
        print(f"Slicing Reverse:   {sliced_reversed}")
        assert reversed_recursive == sliced_reversed, "Reverses do not match!"
        print("Verification passed.\n")