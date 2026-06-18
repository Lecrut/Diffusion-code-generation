import unicodedata

def to_lowercase(text: str) -> str:
    """Convert a string to lowercase using Unicode normalization."""
    if not text:
        return ""
    
    # Normalize unicode characters first (e.g., 'é' vs 'e\u0301')
    normalized = unicodedata.normalize('NFKD', text)
    # Convert to lower case and strip combining marks that might remain
    result = ''.join(c.lower() for c in normalized if not unicodedata.combining(c))
    
    return result

def to_uppercase(text: str) -> str:
    """Convert a string to uppercase using Unicode normalization."""
    if not text:
        return ""
    
    # Normalize unicode characters first (e.g., 'é' vs 'E\u0301')
    normalized = unicodedata.normalize('NFKD', text)
    result = ''.join(c.upper() for c in normalized if not unicodedata.combining(c))
    
    return result

def to_title_case(text: str) -> str:
    """Convert a string to title case (first letter of each word capitalized)."""
    if not text:
        return ""
    
    # Split into words, capitalize first letter of each, then join back
    parts = []
    for part in text.split():
        if len(part) > 0:
            capitalized_part = part[0].upper() + part[1:].lower()
            parts.append(capitalized_part)
    
    return ' '.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    samples = [
        "hello world",
        "PYTHON IS GREAT!",
        "café résumé naïve",  # Unicode test cases
        "",                  # Empty string edge case
        "   multiple   spaces   ",
        "mixedCASE123andSymbols!"
    ]

    print("String Case Manipulation Utilities Test Results")
    print("=" * 50)

    for sample in samples:
        original = repr(sample)
        lower_result = to_lowercase(sample)
        upper_result = to_uppercase(sample)
        title_result = to_title_case(sample)
        
        print(f"\nOriginal Input:\n{original}")
        print("-" * 30)
        print("Lowercase:   ", repr(lower_result))
        print("Uppercase:   ", repr(upper_result))
        print("Title Case:  ", repr(title_result))

    # Performance benchmark simulation (optional internal check, not printed to avoid clutter unless needed)
    import timeit
    
    test_string = "The quick brown fox jumps over the lazy dog" * 1000
    
    t_lower = timeit.timeit('to_lowercase(test_string)', setup='from __main__ import to_lowercase', number=1000)
    t_upper = timeit.timeit('to_uppercase(test_string)', setup='from __main__ import to_uppercase', number=1000)
    t_title = timeit.timeit('to_title_case(test_string)', setup='from __main__ import to_title_case', number=1000)

    print("\n" + "=" * 50)
    print("Performance Benchmark (approximate seconds for 1000 iterations):")
    print(f"To Lowercase:   {t_lower:.4f}s")
    print(f"To Uppercase:   {t_upper:.4f}s")
    print(f"To Title Case:  {t_title:.4f}s")