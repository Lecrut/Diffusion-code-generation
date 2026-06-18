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
    
    # Recursive step: reverse the substring excluding the first character and append the last character to the front
    return reverse_string_recursive(s[1:]) + s[:0]

def analyze_complexity():
    """
    Analyzes time complexity of recursive vs slicing methods.
    
    Time Complexity Analysis:
    - Direct Slicing (s[::-1]): O(n) where n is the length of the string. 
      It creates a new list and then converts it to a string in linear time.
      
    - Recursive Method: T(n) = T(n-1) + O(1). The function makes one recursive call with size n-1,
      performs constant work (string concatenation), which is also O(n) due to creating new strings 
      at each step of the recursion chain. Thus, total time complexity is O(n^2) because string 
      concatenation in Python creates a copy of the result growing up to length n at each level.
    
    Space Complexity:
    - Recursive Method: O(n) for call stack depth plus O(n) for intermediate strings created during concatenation.
    """

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    test_strings = [
        "hello",
        "",
        "a",
        "Python is awesome!",
        "12345"
    ]

    print("Comparing Recursive vs Direct Slicing String Reversal")
    print("=" * 60)

    for s in test_strings:
        # Using direct slicing (O(n))
        reversed_sliced = s[::-1]
        
        # Using recursive method (T(n) ~ O(n^2) due to string concatenation overhead)
        reversed_recursive = reverse_string_recursive(s)
        
        print(f"Input:    '{s}'")
        print(f"Slicing Result:   {reversed_sliced}")
        print(f"Recursive Result: {reversed_recursive}")
        assert reversed_sliced == reversed_recursive, "Results should match!"
        print("-" * 60)

    analyze_complexity()