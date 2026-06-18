import sys
def has_repeated_characters(s: str) -> bool:
    s_lower = s.lower()
    seen_chars = set()
    for char in s_lower:
        if char not in seen_chars:
            seen_chars.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    test_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox"
    ]
    for test_str in test_strings:
        result = has_repeated_characters(test_str)
        if result:
            print(f"'{test_str}' contains repeated characters.")
        else:
            print(f"'{test_str}' does not contain repeated characters.")