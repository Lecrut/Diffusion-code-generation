def has_unique_chars(text: str) -> bool:
    seen = set()
    for char in text:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample_strings = [
        "abcdefg",
        "hello",
        "Python",
        "1234567890",
        "aabbcc"
    ]

    for s in sample_strings:
        result = has_unique_chars(s)
        print(f"has_unique_chars('{s}') = {result}")