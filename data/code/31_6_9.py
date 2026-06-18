import string

def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases such as empty strings
    or those containing only symbols by ignoring non-alphanumeric characters and case differences.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    """
    # Normalize the string by converting to lowercase and removing all non-alphanumeric characters
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    
    return normalized == normalized[::-1]

if __name__ == '__main__':
    sample_values = [
        "",                          # Empty string
        "a",                         # Single character
        "abba",                      # Simple palindrome
        "A man, a plan, a canal: Panama!",  # With symbols and mixed case
        "@#%",                       # Only symbols
        "hello world",               # Not a palindrome (includes space)
        "_!@#",                     # Special characters only
    ]

    print("Palindrome Check Results:")
    for test_str in sample_values:
        result = is_palindrome(test_str)
        status = "is" if result else "is not"
        print(f"'{test_str}' {status} a palindrome")