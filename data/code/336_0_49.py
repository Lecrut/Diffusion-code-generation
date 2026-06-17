def check_repeated_chars(text: str) -> bool:
    lower_text = text.lower()
    seen = set()
    for char in lower_text:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "Hello World!",
        "1234567890"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}': {'Repeated characters found' if result else 'No repeated characters'}")