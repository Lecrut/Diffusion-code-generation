def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces, punctuation, 
    and being case-insensitive.
    
    Parameters:
        text (str): The input string to check.
        
    Returns:
        bool: True if the processed string is a palindrome, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase for comparison
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon.",
        "Hello World!",
        "Madam"
    ]

    for s in sample_strings:
        result = check_palindrome_with_spaces(s)
        print(f"'{s}' is {'a palindrome.' if result else 'NOT a palindrome.'}")