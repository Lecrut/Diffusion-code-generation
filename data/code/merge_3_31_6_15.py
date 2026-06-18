def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, ignoring case, spaces, punctuation, 
    and handling edge cases like empty strings or symbol-only strings.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    """
    # Normalize the string by converting to lowercase and removing non-alphanumeric characters
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    
    # Handle edge cases where empty or symbol-only strings result in an empty normalized string
    return normalized == normalized[::-1]

if __name__ == '__main__':
    test_cases = [
        "",                          # Empty string
        "a",                         # Single character
        "A man, a plan, a canal: Panama",  # Classic palindrome with punctuation and spaces
        "No 'x' in Nixon",           # Palindrome with symbols
        "Not a palindrome",          # Not a palindrome
        "",                          # Explicitly empty again for clarity
        "!@#$%",                     # Only symbols
    ]

    results = []
    for test in test_cases:
        result = is_palindrome(test)
        results.append((test, result))
    
    print("Palindrome Check Results:")
    for original_string, is_palin in results:
        print(f"'{original_string}' -> {is_palin}")