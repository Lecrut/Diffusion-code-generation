def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases like 
    empty strings or strings with non-alphanumeric characters by ignoring 
    case and removing symbols/spaces.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    """
    # Normalize the string: keep only alphanumeric characters and convert to lowercase
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    
    # Handle empty strings or strings with no valid content as palindromes (base case)
    return normalized == normalized[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test edge cases and normal inputs
    samples = [
        "",                          # Empty string
        "a",                         # Single character
        "abba",                      # Simple palindrome
        "A man, a plan, a canal: Panama",  # With spaces and punctuation (classic)
        "No 'x' in Nixon",           # Mixed case with symbols
        "!@#$%",                     # Only symbols
        "",                          # Repeated empty string check
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"Input: '{sample}' -> Is Palindrome: {result}")