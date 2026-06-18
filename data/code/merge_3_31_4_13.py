def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation,
    and being case-insensitive.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "Madam"
    ]

    for test_string in sample_strings:
        result = check_palindrome_with_spaces(test_string)
        print(f"'{test_string}' is {'a' if result else 'not'} a palindrome.")