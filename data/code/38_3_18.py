def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are any repeating letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        # Only consider alphabetic characters and ignore non-letters like spaces or punctuation
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        "hello",      # Should be True (e, l, o repeat)
        "abcdefg",   # Should be False (all unique)
        "The quick brown fox jumps over the lazy dog.",  # Should be True ('t', 'h' appear multiple times if case-insensitive and we count spaces/punctuation? Task says letters only. Let's re-evaluate: 'the' has t,h,e; 'over' o,v,r,e... Wait, standard interpretation is just alphabetic chars.)
        "a",          # Should be False
        "",           # Should be False
    ]

    for test_str in test_cases:
        result = contains_repeated_letters(test_str)
        print(f"String: '{test_str}' -> Contains repeated letters: {result}")