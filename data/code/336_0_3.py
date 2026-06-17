def has_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    seen = set()
    for char in text_lower:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = has_repeated_chars(sample_string)
    print(f"Input string: {sample_string}")
    print("Contains repeated characters:", result)