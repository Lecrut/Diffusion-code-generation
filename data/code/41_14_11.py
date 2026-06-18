import unicodedata

def to_lowercase(text: str) -> str:
    """Converts a string to lowercase using Unicode normalization."""
    if not text:
        return ""
    
    # Normalize form 'NFKD' to handle compatibility characters, then fold case
    normalized = unicodedata.normalize('NFKD', text)
    result = "".join(c.lower() for c in normalized)
    return result

def to_uppercase(text: str) -> str:
    """Converts a string to uppercase using Unicode normalization."""
    if not text:
        return ""
    
    # Normalize form 'NFKC' (compatibility composition) then fold case
    normalized = unicodedata.normalize('NFKC', text)
    result = "".join(c.upper() for c in normalized)
    return result

def to_title_case(text: str) -> str:
    """Converts a string to title case."""
    if not text:
        return ""
    
    # Split into words based on whitespace and other non-alphanumeric boundaries,
    # capitalize the first letter of each word, then join.
    parts = []
    current_word_start = False
    
    for char in text:
        is_alpha = unicodedata.category(char).startswith('L')  # Letter category
        
        if not is_alpha and (not current_word_start or char.isalnum()):
            # Start of a new word after non-alphanumeric separator, 
            # unless we are already inside an alphanumeric sequence.
            pass 
        
        elif is_alpha:
            if not current_word_start:
                parts.append(char.upper())
                current_word_start = True

if __name__ == '__main__':
    pass
