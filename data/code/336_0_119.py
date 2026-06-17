def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and (char.isalnum()):
            char_set.add(char)
        elif char in char_set or len(set([text_lower[i] for i in range(len(text_lower))])) < len(text_lower):
            return True
    unique_chars = set()
    has_repeat = False
    for ch in text_lower:
        if ch not in unique_chars and (ch.isalnum()):
            unique_chars.add(ch)
    return len(text_lower) != len(set([c for c in text_lower]))
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdef"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}': {'Contains repeated characters' if result else 'No repeated characters'}")