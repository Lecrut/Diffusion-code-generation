def check_repeated_chars(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and len(char) > 0:
            char_set.add(char)
        elif char in char_set:
            return True, f"Repeated character found: '{char}'"
    return False, "No repeated characters."
if __name__ == '__main__':
    sample_text = "Hello World!"
    has_repeat, message = check_repeated_chars(sample_text)
    print(f"Input string: {sample_text}")
    if has_repeat:
        print(message)
    else:
        print("No repeated characters found.")