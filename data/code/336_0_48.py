def check_repeated_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 0
        else:
            return True, f"Repeated character found: '{char}'"
    return False, "No repeated characters found."
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg",
        "The quick brown fox jumps over the lazy dog"
    ]
    for s in sample_strings:
        has_repeat, message = check_repeated_characters(s)
        print(f"'{s}': {message}")