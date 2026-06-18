import string

def is_palindrome(s: str) -> bool:
    """
    Check if a given string (ignoring spaces, punctuation, and case differences) 
    reads the same forwards and backwards.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if it is a palindrome after cleaning, False otherwise.
    """
    # Create cleaned version of the string by removing non-alphanumeric characters 
    # and converting text to lowercase.
    clean_s = ''.join(char.lower() for char in s if char.isalnum())

    return clean_s == clean_s[::-1]

if __name__ == '__main__':
    pass
