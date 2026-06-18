import sys
def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if char not in char_count:
            char_count[char] = 0
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "abcdefg",
        "AaBbCcDdEeFfGg"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}': {'Repeated characters found' if result else 'No repeated characters'}")