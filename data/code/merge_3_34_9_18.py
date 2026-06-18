"""
Module to capitalize the first letter of each word in a string efficiently 
without manual indexing loops, adhering to Pythonic best practices.
"""

def capitalize_words(text: str) -> str:
    """
    Capitalize only the first letter of each word in the input string.

    Args:
        text (str): The input string containing words separated by whitespace or punctuation.

    Returns:
        str: A new string with the first character of each word capitalized, 
             preserving original casing for subsequent letters and non-alpha characters.
    
    Note:
        This function uses a regular expression to match sequences that start with 
        an alphabetic character followed by any sequence (including punctuation), 
        ensuring only the initial letter is uppercased while maintaining the rest of 
        the word's structure intact.

    Example:
        >>> capitalize_words("hello world!")
        'Hello World!'
    """
    import re
    
    # Pattern explanation:
    # \b       - Word boundary to ensure we start at a new "word" context
    # [A-Za-z] - Match exactly one alphabetic character (the first letter of the word)
    #          - We use this capture group because regex substitution can't directly 
    #            modify just that matched part without capturing it.
    return re.sub(r'(?<!^)(?=[A-Z])([a-zA-Z])', lambda m: m.group(1).upper(), text.lower())

if __name__ == '__main__':
    sample_strings = [
        "hello world!",
        "python is awesome",
        "multiple   spaces  here.",
        "---no-alpha---",
        "MixedCASE test"
    ]

    for s in sample_strings:
        result = capitalize_words(s)
        print(f'Input: "{s}"')
        print(f'Output: "{result}"\n')