import re

def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Handles edge cases such as empty strings and strings containing only symbols correctly.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string by converting to lowercase
    normalized = s.lower()
    
    # Filter out non-alphanumeric characters and keep only digits and letters
    cleaned = ''.join(char for char in normalized if char.isalnum())
    
    # If no alphanumeric characters remain after cleaning, treat it as a palindrome (e.g., "!!!") 
    # based on the strict definition where an empty or symbol-only string reads the same forward/backward.
    # However, typically edge cases like symbols only are considered palindromes if we ignore them entirely.
    
    return cleaned == reversed(cleaned)

if __name__ == '__main__':
    # Hard-coded sample values to test various scenarios including empty strings and symbol-only strings
    samples = [
        "",                          # Empty string - should be True (empty reads same as itself)
        "a",                         # Single character - should be True
        "12321",                     # Numeric palindrome - should be True
        "A man a plan a canal Panama!",  # Case and non-alphanumeric mix - should be True
        "hello world",               # Not a palindrome - should be False
        "!!!",                       # Symbols only - treated as empty alphanumeric -> True
        "@#$%",                      # Only symbols - True
        "12345",                     # No symmetry in numbers - False
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")