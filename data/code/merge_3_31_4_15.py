def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation,
    and being case-insensitive.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the filtered text is equal to its reverse
    return filtered_text == filtered_text[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon.",
        "Hello World"
    ]

    for s in sample_strings:
        result = check_palindrome_with_spaces(s)
        print(f"'{s}' is {'a palindrome' if result else 'NOT a palindrome'}")