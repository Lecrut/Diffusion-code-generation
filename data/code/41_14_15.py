import unicodedata

def to_lowercase(s: str) -> str:
    """Convert a string to lowercase using optimized Unicode normalization."""
    # Normalize unicode characters (e.g., é -> e) before lowercasing
    normalized = unicodedata.normalize('NFKD', s)
    return normalized.lower()

def to_uppercase(s: str) -> str:
    """Convert a string to uppercase using optimized Unicode normalization."""
    normalized = unicodedata.normalize('NFKD', s)
    return normalized.upper()

def to_title_case(s: str) -> str:
    """Convert a string to title case (first letter of each word capitalized)."""
    # Normalize and split into words, capitalizing the first letter of each
    normalized = unicodedata.normalize('NFKD', s)
    return ' '.join(word.capitalize() for word in normalized.split())

if __name__ == '__main__':
    sample_strings = [
        "hELLO wORLD",
        "café résumé naïve",
        "this is a test string with mixed CASE",
        "",
        "   multiple spaces and tabs\tand newlines\n"
    ]

    print("Original | Lowercase      | Uppercase       | Title Case")
    print("-" * 105)

    for text in sample_strings:
        lower = to_lowercase(text)
        upper = to_uppercase(text)
        title = to_title_case(text)
        
        # Truncate output if string is too long for display purposes, 
        # but ensure the logic remains intact.
        short_str = f"{text[:30]}..." if len(text) > 35 else text
        
        print(f'{short_str:<41} | {lower:<26} | {upper:<27} | {title}')

    # Verify edge cases explicitly mentioned in the logic flow
    assert to_lowercase("") == ""
    assert to_uppercase("") == ""
    assert to_title_case("") == ""
    
    print("\nAll assertions passed successfully.")