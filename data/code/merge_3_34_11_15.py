import re

def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes only the first character of every word in the input string.
    
    This implementation uses a regular expression to find all words and replaces 
    them with their capitalized versions, which is generally more efficient for 
    varying lengths than manual iteration for large strings due to optimized C-level operations.

    Args:
        text (str): The input string containing multiple words separated by whitespace or other delimiters.
        
    Returns:
        str: A new string where the first character of each word is capitalized, and all subsequent characters 
             within that word are lowercase. Non-word characters remain unchanged except for their position relative to words.
             
    Example:
        >>> capitalize_first_letter_only("hello world")
        'Hello World'
        >>> capitalize_first_letter_only("  python3 code ")
        '  Python3 Code '
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Use regex to find all words. \w+ matches sequences of alphanumeric characters and underscores.
    # We replace each word with itself capitalized (first char upper, rest lower).
    return re.sub(r'\b\w+\b', lambda match: match.group(0)[0].upper() + match.group(1).lower(), text)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "  python3 code ",
        "python-is-great-and-so-are-codes",
        "",
        "singleword"
    ]

    for s in sample_strings:
        result = capitalize_first_letter_only(s)
        print(f'Input: "{s}" -> Output: "{result}"')