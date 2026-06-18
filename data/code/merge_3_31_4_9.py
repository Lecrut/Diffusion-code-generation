def check_palindrome_with_spaces(text):
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation,
    and being case-insensitive.

    Parameters:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Normalize to lowercase and remove non-alphanumeric characters except digits/letters
    cleaned_chars = [c.lower() for c in text]
    
    # Keep only alphanumeric characters (a-z, A-Z, 0-9)
    filtered_chars = ''.join(c if c.isalnum() else '' for c in reversed(cleaned_chars))

# Note: The logic above was slightly inverted in the list comprehension thought process. 
# Let's correct it directly below by filtering first then reversing or just iterate from both ends after cleaning all alphanumeric characters.
    # Correct Approach: Clean only alphanumerics, make lowercase, then check palindrome property.
    
    cleaned_string = ''.join(c.lower() for c in text if c.isalnum())

    return cleaned_string == reversed(cleaned_string)

if __name__ == '__main__':
    sample_tests = [
        "A man a plan a canal Panama",
        "No 'x' in Nixon.",
        "Madam, I'm Adam!",
        "Was it a car or a cat I saw?",
        "Hello World",
    ]

    for test_input in sample_tests:
        result = check_palindrome_with_spaces(test_input)
        print(f"Input: {test_input!r}")
        print(f"Is Palindrome (ignoring spaces/punctuation, case-insensitive): {result}\n")