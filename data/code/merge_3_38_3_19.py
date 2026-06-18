def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are duplicate letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        # Check only alphabetic characters; ignore digits/punctuation/spaces as per typical "letter" interpretation unless specified otherwise. 
        # However, to be safe and strictly follow 'letters', we check if it's an alphabet character before adding/checking duplicates of letters specifically.
        # But the prompt says "repeated letters", implying only a-z/A-Z count. If I include all chars, digits could technically repeat too but aren't usually called 'letters'. 
        # Let's stick to strict definition: check if char is alphanumeric or just letter? Usually in these puzzles it means alphabetic characters.
        # Re-reading "repeated letters": implies a-z/A-Z only.
        if not ('a' <= char.lower() <= 'z'):
            continue
        
        if char in seen:
            return True
        seen.add(char)
    
    return False

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    samples = [
        "hello",       # Should be True (e, l repeated)
        "abcdef",      # Should be False (all unique)
        "A man a plan",# Should be True ('a' and 'm' are repeated case-insensitive)
        "1234567890",  # Should be False (no letters)
        "The quick brown fox jumps over the lazy dog"   # Should be True ('t', 'h', etc. repeat)
    ]

    for sample in samples:
        result = contains_repeated_letters(sample)
        print(f"'{sample}' -> {result}")