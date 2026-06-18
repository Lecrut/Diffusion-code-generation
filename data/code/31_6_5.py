def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases like empty strings 
    or strings containing only symbols (non-alphanumeric characters).
    
    The comparison considers only alphanumeric characters and ignores case.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase for uniformity
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # An empty string or one with no alphanumeric chars is technically a palindrome 
    # as it reads the same forwards and backwards.
    return cleaned_s == cleaned_s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test various edge cases without user input
    
    samples = [
        "",                          # Empty string
        "a",                         # Single character
        "abba",                      # Simple palindrome
        "racecar",                   # Classic palindrome
        "A man, a plan, a canal: Panama!",  # With spaces and punctuation (case-insensitive)
        "12321",                     # Numeric palindrome
        "!@#$%",                     # Only symbols
        "",                          # Empty string again for clarity
        "hello world"                # Not a palindrome
    ]

    print("Palindrome Check Results:")
    for sample in samples:
        result = is_palindrome(sample)
        status = "IS" if result else "NOT"
        print(f"'{sample}' -> {status} Palindrome")