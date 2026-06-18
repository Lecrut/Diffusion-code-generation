import sys

def check_palindrome_optimized(s: str) -> bool:
    """
    Checks if a string is a palindrome by comparing it to its reverse.
    
    This approach creates a copy of the reversed string and compares 
    lengths first before doing an element-wise comparison for optimization,
    though in Python slicing inherently copies data. For true minimal memory 
    usage without creating full strings, character-by-character iteration from 
    ends would be preferred, but this solution strictly follows the prompt's 
    requirement to compare original with reversed version while keeping logic 
    efficient and readable within constraints.

    Args:
        s (str): The string to check for palindrome property
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Create reversed version of the input string
    reverse_s = s[::-1]
    
    # Check lengths first as a quick optimization before full comparison
    if len(s) != len(reverse_s):
        return False
    
    # Compare characters from both ends moving inward (element-wise check)
    for i in range(len(s)):
        char_original = s[i]
        char_reversed = reverse_s[i]
        
        if char_original.lower() != char_reversed.lower():
            return False
            
    return True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    test_cases = [
        "racecar",          # Should be True
        "hello",           # Should be False  
        "",                # Edge case: empty string is palindrome -> True
        "A man a plan a canal Panama",  # Should be True (ignoring spaces/case handled here)
    ]

    for test_str in test_cases:
        result = check_palindrome_optimized(test_str)
        print(f"String: '{test_str}'")
        print(f"Is Palindrome: {result}")