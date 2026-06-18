def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation, 
    and being case-insensitive.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the normalized string reads the same forwards and backwards, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase for uniform comparison
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "Madam"
    ]

    print("Palindrome Check Results:\n")
    for test_str in sample_strings:
        result = check_palindrome_with_spaces(test_str)
        print(f'String: "{test_str}" -> {result}')