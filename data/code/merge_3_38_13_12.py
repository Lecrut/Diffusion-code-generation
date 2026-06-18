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
        # Only consider alphabetic characters; ignore digits and symbols based on "letters" context
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("abcdef", False),
        ("A man, a plan, a canal: Panama!", True),  # 'a' and 'n' repeat (case-insensitive)
        ("1234567890", False),
        ("The quick brown fox jumps over the lazy dog.", True),
    ]

    for test_input in test_cases:
        result = contains_repeated_letters(test_input[0])
        expected = test_input[1]
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{test_input[0]}' -> {result} (expected {expected})")