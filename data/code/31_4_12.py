import string

def check_palindrome_with_spaces(s: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces, punctuation,
    and being case-insensitive.

    Parameters:
        s (str): The input string to check.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    clean_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return clean_string == clean_string[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon.",
        "Not a palindrome",
        "Madam In Eden, Sarah!",
        "",
        "   Hello World!   ",
    ]

    for test_string in test_cases:
        result = check_palindrome_with_spaces(test_string)
        print(f"Input: '{test_string}'")
        print(f"Is Palindrome (ignoring spaces/punctuation, case-insensitive): {result}\n")