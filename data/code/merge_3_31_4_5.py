def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation, 
    and being case-insensitive.

    Args:
        text (str): The input string to be checked.

    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    """
    # Convert to lowercase for case-insensitivity
    clean_text = text.lower()
    
    # Remove all non-alphanumeric characters (spaces, punctuation, symbols)
    filtered_chars = [char for char in clean_text if char.isalnum()]
    
    cleaned_string = ''.join(filtered_chars)
    
    return cleaned_string == cleaned_string[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run the function without user input or external dependencies
    test_cases = [
        "A man, a plan, a canal: Panama",  # Should be True
        "race a car",                      # Should be False
        "Was it a cat and I saw a dad?",  # Should be True
        "No 'x' in Nixon",                 # Should be True
        "",                               # Edge case: Empty string, should be True
    ]

    for test_string in test_cases:
        result = check_palindrome_with_spaces(test_string)
        print(f"Input: '{test_string}' -> Is Palindrome: {result}")