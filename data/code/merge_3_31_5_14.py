def is_palindrome(s: str) -> bool:
    """Check if a string (ignoring case but keeping all characters including spaces/punctuation as-is unless specified otherwise). 
       This implementation uses the two-pointer technique to run in O(n) time.
    
    Note: The function considers every character at its original position during comparison, meaning it checks exact equality of substrings from both ends moving inward.
    If you intended case-insensitivity or ignoring non-alphanumeric characters specifically for palindrome logic (e.g., "A man a plan"), 
    please specify those requirements separately as the core two-pointer structure here compares character by character exactly as they appear in s.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Example usage logic: 
        "radar" -> True
        "racecar" -> True
        "abba" -> True
        "abcde" -> False
        
    Note on complexity: O(n) where n is the length of the string, as each character is visited at most once."""

    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    test_cases = [
        ("radar", "Expected: True"),      # Standard palindrome
        ("racecar", "Expected: True"),    # Long palindromic word
        ("abba", "Expected: True"),       # Even length palindrome
        ("not a palindrome", "Expected: False"),  # Contains mismatched chars (e.g., 'n' vs 't')
        ("A man, a plan...", "Expected: True if case/chars normalized; currently False due to exact char match")
    ]

    # To ensure the specific requirement of O(n) checking without ignoring characters:
    # We will check strict character equality first.
    
    for string_val in test_cases[0]: 
        print(f"Input: '{string_val}' -> Output is {is_palindrome(string_val)}")

    # The sample 'A man, a plan...' will actually return False with this exact implementation 
    # because '!' != 'a' or other mismatches exist based on position.
    # If the user wants case-insensitive palindrome ignoring non-alphanumerics specifically:
    
    def is_palindrome_advanced(s):
        """Checks for palindrome considering only alphanumeric characters and ignoring cases."""
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

    print(f"Input: 'A man, a plan...' -> Advanced Output (case-insensitive alphanumeric) is {is_palindrome_advanced('a man,a plan...')}")
    
    # Test advanced function directly with the sample from the list if needed.
    test_str = "a man a plan"
    print(f"Input: '{test_str}' -> Advanced Output is {is_palindrome_advanced(test_str)}")

    result1 = is_palindrome("racecar")
    result2 = is_palindrome("hello")
    
    assert result1 == True, f"Expected 'racecar' to be palindrome. Got {result1}"
    assert result2 == False, f"Expected 'hello' not to be palindrome. Got {result2}"

    print("\nAll basic tests passed.")