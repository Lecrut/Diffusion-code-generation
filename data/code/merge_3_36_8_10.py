def reverse_string_recursive(s):
    """
    Recursively reverses a string.
    
    Base case: if the string is empty, return it as is.
    Recursive step: concatenate the last character with the result of 
    reversing the substring excluding the last character.
    
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
    Analyzes and prints the time complexity of both recursive 
    and direct slicing methods.
    
    This function calculates the number of operations for a given string length
    to demonstrate O(n) vs O(1).
    """
    sample_strings = ["", "a", "ab", "abc", "hello"]
    
    print("Time Complexity Analysis")
    print("-" * 30)
    
    for test_str in sample_strings:
        n = len(test_str)
        
        # Recursive method simulation (actual execution time is negligible 
        # but we analyze the operation count theoretically)
        recursive_ops = n - 1 if n > 0 else 0
        
        # Direct slicing method (s[::-1]) performs in O(1) for indexing,
        # though creating a new string takes O(n). We consider it constant time 
        # relative to recursion depth logic.
        
        print(f"Input Length: {n}")
        print(f"  Recursive Operations Count: {recursive_ops} (Time Complexity: O(n))")
        print(f"  Direct Slicing Ops Count: ~1 (Time Complexity: O(1) for indexing)")
        print()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = ["", "a", "ab", "abc", "hello world"]
    
    time_complexity_analysis()
    
    print("Sample Execution Results:")
    for s in test_cases:
        reversed_s = reverse_string_recursive(s)
        sliced_s = s[::-1]
        
        # Verify correctness of recursive method against slicing (ground truth)
        assert reversed_s == sliced_s, "Recursive reversal failed!"
        
        print(f"Original: '{s}'")
        print(f"Reversed (Rec):  '{reversed_s}'")
        print(f"Reversed (Slice):'{sliced_s}'")
        print("-" * 30)