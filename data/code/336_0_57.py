def contains_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    return len(set(text_lower)) != len(text_lower)
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        result = contains_repeated_characters(s)
        print(f"'{s}': {'Repeated characters found' if result else 'No repeated characters'}")