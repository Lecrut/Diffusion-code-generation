import unicodedata

def to_lowercase(s: str) -> str:
    """Convert a string to lowercase using Unicode normalization for optimal handling."""
    if not s:
        return ""
    
    # Normalize unicode characters first (e.g., 'é' vs 'e\u0301')
    normalized = unicodedata.normalize('NFKD', s)
    return normalized.lower()

def to_uppercase(s: str) -> str:
    """Convert a string to uppercase using Unicode normalization for optimal handling."""
    if not s:
        return ""
    
    # Normalize unicode characters first (e.g., 'é' vs 'E\u0301')
    normalized = unicodedata.normalize('NFKD', s)
    return normalized.upper()

def to_title_case(s: str) -> str:
    """Convert a string to title case using Unicode normalization for optimal handling."""
    if not s:
        return ""
    
    # Normalize unicode characters first (e.g., 'hello world' vs 'Héllo World')
    normalized = unicodedata.normalize('NFKD', s)
    
    result_chars = []
    prev_is_upper = False
    
    for char in normalized:
        is_alpha = char.isalpha()
        
        if not is_alpha:
            # Non-alphabetic characters are kept as-is but don't trigger title case logic immediately after
            result_chars.append(char)
            continue
        
        current_is_upper = char.isupper()
        
        if prev_is_upper and current_is_lower:
            # If previous was uppercase, this should be lowercase (standard title case behavior for words like "Hello" -> 'H' + 'ello')
            # However, standard Python str.title() handles sequences of letters. 
            # We need to ensure we don't double-uppercase or miss the transition logic if there are non-letters in between.
            result_chars.append(char.lower())
        elif not prev_is_upper and current_is_lower:
            # Start of a new word (or after punctuation), make uppercase
            result_chars.append(char.upper())
            
        else:
            # Continue with original case or lowercase if it was already handled by logic above? 
            # Actually, standard title case capitalizes the first letter of each word and lowercases the rest.
            # The logic `prev_is_upper` implies we are in the middle of a "word" started previously.
            result_chars.append(char.lower())
            
        prev_is_upper = current_is_upper
    
    return ''.join(result_chars)

if __name__ == '__main__':
    test_strings = [
        "Hello World!",
        "Python Programming",
        "café résumé naïve",  # Testing Unicode normalization
        "",                  # Edge case: empty string
        "123 ABC xyz",      # Mixed alphanumeric
        "HELLO WORLD"       # All caps input for title case test
    ]

    print("Original | Lowercase | Uppercase | Title Case")
    print("-" * 80)
    
    for s in test_strings:
        lower = to_lowercase(s)
        upper = to_uppercase(s)
        title = to_title_case(s)
        
        # Format output with fixed width columns if possible, otherwise simple join
        formatted_lower = f"{lower:<25}"
        formatted_upper = f"{upper:<20}"
        formatted_title = f"{title:<30}"
        
        print(f"| {s} |")
        print(formatted_lower + " | ")
        print(formatted_upper + " | ")
        print(formatted_title)