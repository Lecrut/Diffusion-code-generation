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
        return reverse_string_recursive(s[1:]) + s[0]

def analyze_complexity():
    """
    Analyzes and prints the time complexity comparison between 
    recursive reversal and direct slicing methods.
    
    Time Complexity Analysis:
    - Recursive Method (reverse_string_recursive): O(n) where n is the length of the string.
      Each call processes one character, leading to a linear number of function calls.
      
    - Direct Slicing ('[::-1]'): O(1).
      Python's slicing creates a new object but does not involve iterative or recursive 
      steps in its internal implementation for simple reversal; it is optimized at the C level.
    
    Space Complexity:
    - Recursive Method: O(n) due to the recursion stack depth required for n characters.
    - Direct Slicing: O(1) auxiliary space (excluding output storage).

    The recursive solution has a higher constant factor and uses more memory compared 
    to direct slicing, although both have linear time complexity in terms of operations performed on data size.
    """
    print("Time Complexity Analysis:")
    n = 500_000  # Sample length for analysis
    
    # Simulate recursive steps (conceptual)
    recursion_steps = sum(1 for _ in range(n)) if True else None 
    slicing_time_op = "O(1)" 
    
    print(f"\nFor a string of length {n}:")
    print("- Recursive method: O(n)")
    print("  - Reasoning: Each character requires one function call, resulting in n calls.")
    print("  - Space Complexity: O(n) due to recursion stack depth.")
    
    print(f"\n- Direct slicing ('[::-1]'): {slicing_time_op}")
    print("  - Reasoning: Internal optimization at the C level avoids explicit loops/recursion.")
    print("  - Space Complexity: O(1) auxiliary (excluding result storage).")

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is needed.
    test_strings = [
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]

    print("Demonstration of Recursive String Reversal:")
    for s in test_strings:
        reversed_s = reverse_string_recursive(s)
        print(f"Original: {s}")
        print(f"Reversed:{reversed_s}\n")
    
    analyze_complexity()