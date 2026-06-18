import unicodedata

def to_lowercase(text: str) -> str:
    """Converts a string to lowercase using Unicode normalization."""
    if not text:
        return ""
    
    # Normalize unicode characters first (e.g., combining diacritics)
    normalized = unicodedata.normalize("NFKD", text).lower()
    return "".join(c for c in normalized if not unicodedata.combining(c))

def to_uppercase(text: str) -> str:
    """Converts a string to uppercase using Unicode normalization."""
    if not text:
        return ""
    
    # Normalize unicode characters first (e.g., combining diacritics)
    normalized = unicodedata.normalize("NFKD", text).upper()
    return "".join(c for c in normalized if not unicodedata.combining(c))

def to_title_case(text: str) -> str:
    """Converts a string to title case (first letter of each word capitalized)."""
    if not text or all(not c.isalpha() for c in text):
        return ""

    # Normalize unicode characters first
    normalized = unicodedata.normalize("NFKD", text)
    
    words = []
    current_word = []
    
    i = 0
    while i < len(normalized):
        char = normalized[i]
        
        if char.isalpha():
            # Check if this is the start of a new word (previous was non-alpha or empty)
            should_capitalize = not current_word
            
            if should_capitalize:
                words.append(char.upper())

if __name__ == '__main__':
    pass
