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
    filtered_chars = [char.lower() for char in text if char.isalnum()]
    
    # Join into a single string for easier comparison or compare directly via slicing
    cleaned_string = "".join(filtered_chars)
    
    return cleaned_string == cleaned_string[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "Hello, World!"
    ]

    for test_input in sample_strings:
        result = check_palindrome_with_spaces(test_input)
        print(f"Input: '{test_input}'")
        print(f"Is Palindrome (ignoring spaces/punctuation/case): {result}\n")