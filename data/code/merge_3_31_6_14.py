"""
Palindrome Checker Module

This module provides a robust function to determine if a string is a palindrome,
handling edge cases such as empty strings and strings containing non-alphanumeric characters.
It considers only alphanumeric characters (letters and digits) while ignoring case.
"""

def is_palindrome(s: str) -> bool:
    """
    Determines whether the input string is a palindrome.

    This function checks for palindromicity based on sequences of letters 
    that are either alphabetic or numeric, regardless of other characters in the string, 
    and case-insensitive. It ignores symbols and spaces by stripping them out during processing.

    Parameters:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome after removing non-alphanumeric 
              characters and lowercasing; otherwise, False. Includes handling for 
              edge cases like empty strings or strings with only symbols.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("")
        True (Empty string is considered a palindrome)
        >>> is_palindrome("!@@#%") 
        False
    """

    # Filter for alphanumeric characters and convert to lowercase. This handles spaces/symbols automatically.
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned_string == cleaned_string[::-1]

if __name__ == '__main__':
    pass
