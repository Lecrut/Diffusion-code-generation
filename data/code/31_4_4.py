import string

def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring spaces, punctuation, 
    and case sensitivity.
    
    Parameters:
        text (str): The input string to check.
        
    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered_chars = [char.lower() for char in text if char.isalnum()]
    
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "Not a palindrome"
    ]

    for test_str in sample_strings:
        result = check_palindrome_with_spaces(test_str)
        print(f"'{test_str}' -> {result}")