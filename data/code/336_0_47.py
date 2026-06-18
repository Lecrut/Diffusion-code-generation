def check_repeated_characters(text: str) -> bool:
    lower_text = text.lower()
    seen_chars = set()
    for char in lower_text:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        print(f"'{s}': {'Repeated characters found' if result else 'No repeated characters'}")