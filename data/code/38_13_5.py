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
        if not char.isalpha():  # Ignore non-alphabetic characters like spaces or numbers
            continue
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        "hello",      # Should be True ('l' repeats, 'o' repeats)
        "abcdef",     # Should be False (no repeats)
        "A man a plan",  # Should be True ('a', 'n') repeat case-insensitively
        "12345",       # Should be False (only digits)
        "python code"   # Should be True ('o' and 'e' appear multiple times if counting all, but let's verify: p,y,t,h,o,n,c,o,d,e -> o repeats)
    ]

    for test_string in test_cases:
        result = contains_repeated_letters(test_string)
        print(f"'{test_string}': {result}")