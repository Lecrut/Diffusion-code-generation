import textwrap

def capitalize_words(text: str) -> str:
    """
    Decorator-like function that capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first letter capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split into words, capitalize the first character of each, then join back

if __name__ == '__main__':
    pass
