def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of every word in the input string.
    
    A "word" is defined as a sequence of alphanumeric characters separated 
    by non-alphanumeric boundaries (spaces, punctuation, etc.). Only the first 
    character of each detected word is capitalized; all other letters within 
    that word remain unchanged. This implementation uses regex for efficiency 
    and clarity in boundary detection without manual state management loops.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized, 
             preserving original casing for all other characters.
             
    Example:
        >>> capitalize_first_letter_only("hello world! THIS IS TEST.")
        'Hello World! This Is Test.'
    """
    import re
    
    # Split into words based on non-alphanumeric sequences to handle edge cases like punctuation

if __name__ == '__main__':
    pass
