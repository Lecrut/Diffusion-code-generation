"""Utility functions for string case manipulation."""

def to_lowercase(s: str) -> str:
    """Convert a string to lowercase.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with all characters converted to lowercase.
    """
    return s.lower()

def to_uppercase(s: str) -> str:
    """Convert a string to uppercase.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with all characters converted to uppercase.
    """
    return s.upper()

def to_title_case(s: str) -> str:
    """Convert a string to title case.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string where the first character of each word is uppercase 
             and the rest are lowercase, separated by spaces.
    """
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON IS FUN",
        "this is a sentence with mixed CASE"
    ]

    print("Original:\t\tInput")
    print("Lowercase:\tto_lowercase()")
    print("Uppercase:\tto_uppercase()")
    print("Title Case:\tto_title_case()")
    
    for text in sample_strings:
        print(f"\nSample: '{text}'")
        print(f"  Lowercase: {to_lowercase(text)}")
        print(f" Uppercase: {to_uppercase(text)}")
        print(f" Title Case: {to_title_case(text)}")