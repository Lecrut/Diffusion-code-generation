def reverse_string_recursive(s: str) -> str:
    """
    Recursively reverses a string.
    
    Base case: if the string is empty or has one character, return it as is.
    Recursive step: concatenate the last character with the reversed rest of the string.
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])

def analyze_complexity():
    """
    Analyzes time complexity comparison between recursive and slicing methods.
    
    Recursive approach (reverse_string_recursive):
    - Time Complexity: O(n) where n is the length of the string.
      Each call processes one character, leading to a linear number of function calls.
      However, it has higher constant overhead due to repeated function calls and stack usage.
      
    Slicing approach (s[::-1]):
    - Time Complexity: O(n).
      Python's slicing creates a new string by copying characters in C-level optimization,
      which is highly efficient with low constant factors compared to interpreted recursion.

    Space Complexity Comparison:
    - Recursive: O(n) due to the call stack depth (worst case n frames for length n string).
    - Slicing: O(n) for creating the new reversed string object.
    
    Performance Note:
    While both are theoretically O(n), slicing is typically faster in practice 
    because it avoids Python function call overhead and leverages optimized C implementations.
    """

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_strings = [
        "hello",
        "",
        "a",
        "Python is awesome!",
        "12345"
    ]

    print("Testing Recursive String Reversal")
    for s in test_strings:
        reversed_s_recursive = reverse_string_recursive(s)
        
        # Direct slicing method for comparison (not part of the recursive function requirement, but used for analysis context)
        reversed_s_slice = s[::-1]
        
        print(f"Original: '{s}'")
        print(f"Recursive Result: '{reversed_s_recursive}'")
        print(f"Slicing Result:   '{reversed_s_slice}'")
        assert reversed_s_recursive == reversed_s_slice, "Results do not match!"
        print("-" * 30)

    analyze_complexity()