def has_repeated_characters(text: str) -> bool:
    char_set = set()
    for char in text.lower():
        if char in char_set:
            return True
        char_set.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}': {'Has repeated characters' if result else 'No repeated characters'}")