def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation,
    and being case-insensitive.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered_chars = [char.lower() for char in text if char.isalnum()]
    
    # Check if the list of characters reads the same forwards and backwards
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "Hello World"
    ]

    for test_str in sample_strings:
        result = check_palindrome_with_spaces(test_str)
        print(f"'{test_str}' is {'a palindrome.' if result else 'not a palindrome.'}")