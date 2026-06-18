def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases like 
    empty strings or strings with non-alphanumeric characters by ignoring 
    case and removing those characters during comparison.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    """
    # Normalize the string: keep only alphanumeric characters and convert to lowercase
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string reads the same forwards and backwards
    return normalized == normalized[::-1]

if __name__ == '__main__':
    test_cases = [
        "",                          # Empty string
        "a",                         # Single character
        "abba",                      # Simple palindrome
        "A man, a plan, a canal: Panama",  # Palindrome with punctuation and spaces
        "hello",                     # Not a palindrome
        "!@#$%",                    # Only symbols
        "Was it a car or a cat I saw?",  # Classic tricky case
    ]

    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")