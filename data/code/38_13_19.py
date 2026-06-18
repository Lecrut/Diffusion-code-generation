def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are repeated letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        # Only consider alphabetic characters
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_strings = [
        "hello",      # Should return True ('l' repeats)
        "world",      # Should return False (no repeated letters)
        "programming",# Should return True ('r', 'o', 'a' repeat? Actually: r, o, a, m, i, n, g - wait. p-r-o-g-r-a-m-m-i-n-g -> r repeats, m repeats)
        "abcdefg",    # Should return False (all unique)
        "A man",      # Should return True ('a' and 'n' repeat case-insensitively: A/a, a/n? No. A/m/a/n/ space/space/n/g -> A matches a, n repeats)
        "test"         # Should return True (t/e/s/t - t repeats)
    ]

    for s in sample_strings:
        result = contains_repeated_letters(s)
        print(f"'{s}' has repeated letters: {result}")