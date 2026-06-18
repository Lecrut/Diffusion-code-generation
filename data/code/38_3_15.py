def has_repeated_letters(text: str) -> bool:
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
        ("hello", True),      # h, e, l, o -> l repeats
        ("abcdef", False),    # all unique
        ("AaBbCc", True),     # case-insensitive repeat of A/a and B/b etc. (if logic includes both)
        ("123!@#", False),   # no letters at all based on current strict letter check
        ("python", False),    # p, y, t, h, o, n unique in lowercase? wait 'n' is not repeated here. Correct: False.
                            # Correction: python -> p,y,t,h,o,n are all distinct. So False.
        ("banana", True)      # b,a,n,a,n,a -> a and n repeat multiple times
    ]

    for test_input, expected in test_cases:
        result = has_repeated_letters(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{test_input}' => {result} (expected {expected})")