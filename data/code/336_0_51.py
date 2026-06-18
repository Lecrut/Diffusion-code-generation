def contains_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    return len(set(text_lower)) != len(text_lower)
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "aA123"]
    for s in sample_strings:
        result = contains_repeated_chars(s)
        print(f"String '{s}' has repeated characters: {result}")