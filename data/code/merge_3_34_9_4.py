"""
Module to capitalize the first letter of each word in a string using Pythonic methods.
This script defines a function that splits the input string into words, capitalizes 
the first character of each non-empty part, and rejoins them. It avoids manual indexing loops.
"""

def title_case_words(text: str) -> str:
    """
    Capitalize only the first letter of each word in the given text.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first character of each word capitalized 
             and surrounding whitespace preserved for non-word separators, if applicable via title case logic.
    
    Note:
        This implementation uses a generator expression within list comprehension for efficiency 
        without explicit indexing loops over characters. It splits by any whitespace to handle multiple spaces correctly,
        capitalizing the first letter of each resulting part and then joining them back with single spaces as per standard Pythonic title case behavior unless specific delimiter preservation is needed (here simplified).
    """
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    samples = [
        "hello world this is a test",
        "  multi   spaced   lines in string ",
        "no_change HereCamelCaseShouldBeFixed"
    ]

    for sample_text in samples:
        result = title_case_words(sample_text)
        print(f'Input: "{sample_text}"')
        print(f'Output: "{result}"\n')