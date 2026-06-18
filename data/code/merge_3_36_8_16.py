def reverse_string_recursive(s: str) -> str:
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
    Analyzes the time complexity of the recursive solution compared to slicing.
    
    Recursive Solution (reverse_string_recursive):
    - Time Complexity: O(n) where n is the length of the string.
      Each call processes one character and makes a recursive call with size n-1,
      resulting in n calls total. The concatenation at each step takes O(k) time 
      for k characters remaining, but amortized over all steps it remains linear.
    - Space Complexity: O(n) due to the recursion stack depth of n frames.
    
    Direct Slicing (s[::-1]):
    - Time Complexity: O(n). Python's slicing creates a new string by copying 
      characters in a single pass, which is highly optimized in CPython.
    - Space Complexity: O(n) for creating the reversed copy plus negligible overhead.
    
    Comparison:
    Both methods have linear time complexity O(n). However, the recursive approach 
    has higher constant factors due to function call overhead and string concatenation 
      logic compared to Python's optimized slicing implementation. The space complexity 
    is similar (O(n)), but recursion adds potential stack overflow risks for very long strings.
    
    For practical purposes in Python, direct slicing is preferred for performance and safety.
    """

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        "hello",
        "",
        "a",
        "Python Programming",
        "12345"
    ]

    print("Recursive Reversal Results:")
    for text in test_cases:
        reversed_text = reverse_string_recursive(text)
        print(f'Original: "{text}" -> Reversed: "{reversed_text}"')

    analyze_complexity()  # Print the analysis output to console