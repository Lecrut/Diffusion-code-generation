def check_repeated_chars(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if not (char.isalnum()):
            continue
        if char in char_set:
            return True, f"Repeated character found: '{char}'"
        char_set.add(char)
    return False, "No repeated characters found."
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    has_repeat, message = check_repeated_chars(sample_text)
    print(f"Input: {sample_text}")
    if has_repeat:
        print(message)
    else:
        print("No repeated characters found.")