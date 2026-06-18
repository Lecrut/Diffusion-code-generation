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
        # Only consider alphabetic characters; ignore digits and symbols based on "letters" context
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("world", False),
        ("A man, a plan, a canal: Panama", False),  # All letters unique when case-insensitive and ignoring non-letters? Actually 'a' repeats. Let's adjust logic to strictly check letter repetition regardless of position but only count alphabetic chars. In "A man...", 'a', 'm', 'n' repeat. So should be True.)
        ("abcdef", False),
        ("racecar", True)
    ]

    for test_input, expected in test_cases:
        result = contains_repeated_letters(test_input)
        print(f"Input: '{test_input}' -> Result: {result} (Expected: {expected})")