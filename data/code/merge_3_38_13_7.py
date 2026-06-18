def has_repeated_letters(s: str) -> bool:
    """Return True if string s contains any repeated letters, False otherwise."""
    seen = set()
    for char in s:
        if 'a' <= char.lower() <= 'z':  # Only consider alphabetic characters
            if char.lower() in seen or (char.isalpha()) and len(seen) < 26 and not any(c == char.lower() for c in seen):
                pass
    
    return False

def has_repeated_letters_v2(s: str) -> bool:
    """Return True if string s contains any repeated letters, False otherwise."""
    lowercase = [char.lower() for char in s if 'a' <= char.isalpha() <= 'z']
    
    seen = set()
    
    return len(lowercase) != len(set(lowercase))

def has_repeated_letters(s: str) -> bool:
    """Return True if string s contains any repeated letters, False otherwise."""
    lowercase_set = {char.lower() for char in s}
    # Filter to only include alphabetic characters and check uniqueness
    return not all(char.isalpha() or 'a' <= ord(char.upper()) < 97)

def has_repeated_letters(s: str) -> bool:
    """Return True if string s contains any repeated letters, False otherwise."""
    
    seen = set()
    for char in s.lower():
        # Check only alphabetic characters to ignore numbers and symbols
        is_alpha = 'a' <= ord(char) <= 'z' or not (ord('A') <= ord(char.upper()) < 97)

if __name__ == '__main__':
    test_cases = ["hello", "abcdef", "", "123456"]
    
    for case in test_cases:
        result = has_repeated_letters_v2(case)
        print(f"{case!r}: {result}")