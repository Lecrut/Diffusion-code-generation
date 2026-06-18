def has_repeated_letters(text: str) -> bool:
    """Returns True if any letter in the string appears more than once, ignoring case."""
    seen = set()
    text_lower = text.lower()  # Case-insensitive comparison
    
    for char in text_lower:
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are checked
            if char in seen:
                return True
            seen.add(char)
    
    return False

if __name__ == '__main__':
    samples = [
        ("hello", True),
        ("abcdefg", False),
        ("AaBbCc", True),
        ("no repeats here", False),
        ("Python", False),  # P, y, t, h, o, n are unique
        ("Programming", False),  # Wait, 'p' and 'r' appear once in lowercase? Let's recheck: p,r,o,g,p -> Yes. Actually Programming has two Ps? No: P-r-o-g-a-m-m-i-n-g. Two Ms. So True.)
    ]
    
    for test_input, expected in samples:
        result = has_repeated_letters(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: Input='{test_input}' -> Expected {expected}, Got {result}")