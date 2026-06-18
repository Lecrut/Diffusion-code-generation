def has_repeated_letters(s: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if there are duplicate letters, False otherwise.
    """
    seen = set()
    for char in s.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters a-z
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("abcdef", False),
        ("AaBbCc", True),
        ("123!@#", False),
        ("python", False),
        ("programming", True)
    ]

    for text, expected in test_cases:
        result = has_repeated_letters(text)
        print(f"Input: '{text}' -> Expected: {expected}, Got: {result}")