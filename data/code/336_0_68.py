def has_repeated_chars(text: str) -> bool:
    text = text.lower()
    seen = set()
    for char in text:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "aabbcc"]
    for s in sample_strings:
        result = has_repeated_chars(s)
        print(f"'{s}': {'Has repeated characters' if result else 'No repeated characters'}")