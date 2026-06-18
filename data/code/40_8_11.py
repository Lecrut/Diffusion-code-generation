def extract_first_letters(text: str) -> list[str]:
    """
    Extracts a list of strings, where each string is the first letter 
    of a word in the input text. Words containing only punctuation are ignored.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the 
                   first letters of valid words.
    """
    import re
    
    # Split the text into tokens based on whitespace and punctuation boundaries
    # We use a regex that treats any non-letter character as a separator,
    # but we need to be careful with contractions or attached symbols.
    # A robust approach is to split by non-alphanumeric characters first, 
    # then filter out empty strings resulting from consecutive separators.
    
    tokens = re.split(r'[^a-zA-Z0-9]+', text)
    
    result_list = []
    
    for token in tokens:
        if not token or len(token) == 1 and not any(c.isalpha() for c in token):
            # Skip empty strings or single non-alphabetic characters (punctuation only)
            continue
        
        first_char = token[0]
        
        # Ensure the character is actually a letter to be safe,

if __name__ == '__main__':
    pass
