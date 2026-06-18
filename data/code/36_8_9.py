def reverse_string_recursive(s: str) -> str:
    """
    Recursively reverses a string without using slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Base case: if the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    
    # Recursive step: reverse the substring starting from index 1 and append the first character at the end
    return reverse_string_recursive(s[1:]) + s[:1]

def analyze_complexity():
    """
    Analyzes time complexity of recursive vs slicing methods.
    
    Time Complexity Analysis:
    - Recursive Method (reverse_string_recursive): O(n) where n is the length of the string.
      Each call processes one character and reduces the problem size by 1 until reaching base case.
      
    - Slicing Method (s[::-1]): O(1) for slicing operation itself, but creating a new reversed 
      string requires copying all characters: O(n). Total time complexity is also O(n), 
      though with lower constant factors due to optimized C implementation in Python.
    
    Space Complexity Analysis:
    - Recursive Method: O(n) stack space required for recursion depth.
    - Slicing Method: O(1) auxiliary space (excluding the new string storage).

    The recursive solution has better conceptual clarity but uses more memory 
    due to call stack overhead, while slicing is generally faster in practice.
    """

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        "hello",
        "",
        "a",
        "Python Programming",
        "12345"
    ]
    
    print("Testing Recursive String Reversal:")
    print("-" * 40)
    
    for text in test_cases:
        reversed_text = reverse_string_recursive(text)
        slice_reversed = text[::-1] if len(text) > 0 else ""
        
        match_status = "✓ Matched" if reversed_text == slice_reversed else "✗ Mismatch"
        print(f"Input:    '{text}'")
        print(f"Recursive : '{reversed_text}' ({match_status})")
        print("-" * 40)
    
    # Complexity analysis output (formatted as text for clarity)
    complexity_note = """
Time Complexity Comparison:
- Recursive Solution: O(n) - Linear time due to n recursive calls.
- Slicing Method:     O(n) - Single pass through data but optimized implementation.

Space Complexity Note:
- Recursive:          O(n) stack frames for deep recursion.
- Slicing:            O(1) extra space (result string storage excluded).

The slicing method is typically preferred in production due to lower overhead,
while the recursive approach demonstrates algorithmic concepts clearly."""
    print(complexity_note.strip())