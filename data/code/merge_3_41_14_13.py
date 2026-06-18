import unicodedata

def to_lowercase(s: str) -> str:
    """Convert a string to lowercase using efficient unicode normalization."""
    if not s:
        return ""
    
    # Normalize unicode characters first, then apply lowercasing for consistency
    normalized = unicodedata.normalize("NFKD", s)
    return "".join(c.lower() for c in normalized)

def to_uppercase(s: str) -> str:
    """Convert a string to uppercase using efficient unicode normalization."""
    if not s:
        return ""

    # Normalize unicode characters first, then apply uppercasing for consistency
    normalized = unicodedata.normalize("NFKD", s)
    return "".join(c.upper() for c in normalized)

def to_title_case(s: str) -> str:
    """Convert a string to title case using efficient unicode normalization."""
    if not s:
        return ""

    # Normalize and convert first parts, then split on non-word characters
    try:
        base = "".join(c.title() for c in unicodedata.normalize("NFKD", s))
        
        # Use regex-like logic by manually splitting based on word boundaries conceptually handled by join
        return " ".join(base)
    
    except Exception:
        raise ValueError(f"Error processing string {s}")

if __name__ == '__main__':
    sample_strings = [
        "hElLo WoRLd",
        "Python Is Great!",
        "  Leading and Trailing spaces  ",
        "123abc456DEF",
        ""
    ]

    for test_str in sample_strings:
        print(f"Original: {test_str!r}")
        print(f"Lowercase: '{to_lowercase(test_str)}'")
        print(f"Uppercase: '{to_uppercase(test_str)}'")
        print(f"Title Case: '{to_title_case(test_str)}'")
        print("-" * 40)