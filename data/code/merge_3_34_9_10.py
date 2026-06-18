"""
Module to capitalize the first letter of each word in a string efficiently 
without manual indexing loops, adhering to Pythonic best practices.
"""

def title_case_string(text: str) -> str:
    """
    Capitalize only the first letter of each word in the input string.

    This function uses the built-in `str.title()` method which is optimized 
    and handles edge cases like multiple spaces, punctuation, and unicode characters correctly.
    
    Args:
        text (str): The input string to be processed.
        
    Returns:
        str: A new string with each word's first letter capitalized.
    """
    return text.title()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = [
        "hello world",
        "python is awesome!",
        "  multiple   spaces ",
        "mixed CASE string",
        "unicode: café résumé"
    ]

    for original in samples:
        result = title_case_string(original)
        print(f'Original: "{original}"')
        print(f'Titled:   "{result}"\n')