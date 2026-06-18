def contains_repeated_letters(s: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if there are repeating letters, False otherwise.
    """
    seen_letters = set()
    for char in s.lower():
        # Check only alphabetic characters; ignore digits and symbols per task implication of 'letters'
        if not char.isalpha():
            continue
        
        if char in seen_letters:
            return True
        seen_letters.add(char)
    
    return False

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "hello",      # Should return True ('l' repeats, 'o' repeats)
        "world",      # Should return False (all unique letters: w,o,r,l,d)
        "abc123xyz",  # Should return False (no repeated alphabetic characters)
        "AaBbCc",     # Should return True (case-insensitive repetition of A/a, B/b, C/c)
        "pythoncode"  # Should return False (p,y,t,h,o,n,c,d,e are all unique in lowercase)
    ]

    for test_str in samples:
        result = contains_repeated_letters(test_str)
        print(f"'{test_str}': {result}")