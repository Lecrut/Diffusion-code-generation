def check_palindrome_with_spaces(s: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation,
    and being case-insensitive.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Create a list of lowercase characters that are alphanumeric or space-removed punctuation
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    # Check if the sequence reads the same forwards and backwards
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "Not a palindrome!",
        "Madam",
        ""
    ]

    for test_string in test_cases:
        result = check_palindrome_with_spaces(test_string)
        print(f"Input: '{test_string}'")
        print(f"Is Palindrome (ignoring spaces/punctuation, case-insensitive): {result}\n")