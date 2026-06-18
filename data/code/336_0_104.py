def check_repeated_characters(text):
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
    sample_text = "Hello World!"
    has_repeats, message = check_repeated_characters(sample_text)
    print(f"Input: {sample_text}")
    print(message if not has_repeats else f"{message} - Repeated characters detected.")