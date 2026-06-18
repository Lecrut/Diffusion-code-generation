def contains_repeated_chars(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if not (char.isalpha()):
            continue
        if char in char_set:
            return True, f"Repeated character found: '{char}'"
        char_set.add(char)
    return False, "No repeated characters found."
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        has_repeat, message = contains_repeated_chars(s)
        print(f"'{s}': {message}")