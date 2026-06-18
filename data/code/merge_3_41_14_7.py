import unicodedata

def to_lowercase(text: str) -> str:
    """Converts a string to lowercase without external libraries."""
    return text.lower() if not isinstance(text, str) else text.lower()

def to_uppercase(text: str) -> str:
    """Converts a string to uppercase handling Unicode correctly."""
    normalized = unicodedata.normalize('NFD', text)
    result = ''.join(char.upper() for char in normalized)
    return unicodedata.normalize('NFDC', result)

def to_title_case(text: str) -> str:
    """Converts a string to title case, capitalizing the first letter of each word."""
    if not text or not isinstance(text, str):
        return ""
    
    # Split into words based on whitespace
    parts = []
    for part in text.split():
        # Handle non-alphabetic characters by keeping them as is but splitting logic handles spaces
        # Capitalize only the first character if it exists and is a letter or number start point
        new_part = ""
        for i, char in enumerate(part):
            if i == 0:
                # Check for leading punctuation handling (keep original) then capitalize next part if alphanumeric starts? 
                # For standard title case, we just capitalize the first character of each word.
                pass
            
            new_part += char
        parts.append(new_part)

    return ' '.join([p.capitalize() for p in parts])

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON PROGRAMMING LANGUAGE",
        "mIxEd CaSe wItH SpEcIaL cHaRs!",
        "🌍 unicode test case"
    ]

    print("Original: 'hello world' -> Lowercase:", to_lowercase(sample_strings[0]))
    print("Original: 'PYTHON PROGRAMMING LANGUAGE' -> Uppercase:", to_uppercase(sample_strings[1]))
    print("Original: 'mIxEd CaSe wItH SpEcIaL cHaRs!' -> Title Case:", to_title_case(sample_strings[2]))
    
    for s in sample_strings:
        if len(s) > 80 or '\n' in str(s): # avoid very long lines in raw output unless handled carefully
            continue
    
    print("Originals printed above.")