def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases like 
    empty strings or strings with only symbols (non-alphanumeric characters).
    
    The comparison considers only alphanumeric characters and ignores case.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase for uniformity
    cleaned_chars = [c.lower() for c in s if c.isalnum()]
    
    # An empty list (from an empty or symbol-only string) is considered a palindrome
    return cleaned_chars == cleaned_chars[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test edge cases and normal scenarios
    samples = [
        "",                          # Empty string
        "a",                         # Single character
        "abba",                      # Simple palindrome
        "racecar",                   # Classic palindrome
        "!_!@_",                     # String with only symbols (should be True)
        "A man, a plan...",          # Palindrome with punctuation and spaces (should be False due to 'a' vs '.' logic if not filtered correctly, but our filter handles it. Note: original phrase is usually 'A man, a plan, a canal: Panama'. Let's use the standard one)
        "A man, a plan, a canal: Panama", # Standard palindrome with punctuation/spaces (should be True)
        "hello world!",              # Not a palindrome
    ]

    for test_str in samples:
        result = is_palindrome(test_str)
        print(f"Input: '{test_str}' -> Is Palindrome: {result}")