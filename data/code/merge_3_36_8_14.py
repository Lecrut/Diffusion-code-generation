def reverse_string_recursive(s: str) -> str:
    """
    Recursively reverses a string.
    
    Base case: if the string is empty or has one character, return it as is.
    Recursive step: concatenate the last character with the reversed rest of the string.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: The reversed string.
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])

def time_complexity_analysis():
    """
    Analyzes and prints the time complexity comparison between 
    recursive reversal and direct slicing.
    
    Both methods have O(n) time complexity, but with different constant factors.
    - Recursive: Higher overhead due to function call stack management.
    - Slicing (s[::-1]): Lower overhead, implemented efficiently in CPython using optimized loops/C code internally.
    """
    print("Time Complexity Analysis:")
    print("========================")
    
    # Both methods process each character exactly once for the core logic of reversal.
    n = len('Hello World')  # Using a sample length
    
    # Recursive approach: T(n) = T(n-1) + O(1). Total steps ~ n function calls.
    recursive_time_estimate = "O(n)" 
    slicing_time_estimate = "O(n)" 
    
    print(f"\nInput string length (approximate): {len('Hello World')}")
    
    # Detailed breakdown for the user based on algorithmic structure:
    print("\n1. Recursive Solution:")
    print("   - Logic: T(n) = 1 + T(n-1)")
    print("   - Each character requires a function call and concatenation.")
    print(f"   - Total Operations ~ {len('Hello World')} recursive calls.")
    
    print("\n2. Direct Slicing (s[::-1]):")
    print("   - Logic: Implemented in CPython as an optimized loop or built-in operation.")
    # While logically O(n), the constant factor is significantly smaller than recursion due to lack of stack overhead.
    print(f"   - Total Operations ~ {len('Hello World')} character moves (internal implementation).")
    
    print("\n3. Comparison:")
    print("   - Time Complexity: Both are linear, T(n) = O(n).")
    print("   - Space Complexity: Recursive is O(n) due to call stack; Slicing is effectively O(1) auxiliary space (excluding result storage).")
    print("   - Performance: Direct slicing is faster in practice for large strings.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    
    test_string = "Hello World"
    
    print(f"Original String: {test_string}")
    
    reversed_recursive = reverse_string_recursive(test_string)
    reversed_slicing = test_string[::-1]
    
    print(f"\nReversed (Recursive):  {reversed_recursive}")
    print(f"Reversed (Slicing):    {reversed_slicing}")
    
    assert reversed_recursive == reversed_slicing, "Results must match!"
    
    time_complexity_analysis()