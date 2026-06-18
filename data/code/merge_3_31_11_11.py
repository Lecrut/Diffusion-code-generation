def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race car",
        "hello world",
        "Madam",
        ""
    ]

    for text in test_cases:
        result = is_palindrome(text)
        status = "is" if result else "is not"
        print(f"'{text}' {status} a palindrome.")