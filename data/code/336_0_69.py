import sys
def has_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    seen_characters = set()
    for char in text_lower:
        if char in seen_characters:
            return True
        seen_characters.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox"
    ]
    for test_string in sample_strings:
        result = has_repeated_chars(test_string)
        if result:
            print(f"'{test_string}' contains repeated characters.")
        else:
            print(f"'{test_string}' does not contain repeated characters.")
    sys.exit(0)