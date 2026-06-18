def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    seen = set()
    for char in text_lower:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}' contains repeated characters: {result}")