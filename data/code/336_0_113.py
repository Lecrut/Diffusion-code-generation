def has_repeated_characters(text):
    text_lower = text.lower()
    seen_chars = set()
    for char in text_lower:
        if char not in seen_chars:
            seen_chars.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = has_repeated_characters(sample_string)
    if result:
        print(f"The string '{sample_string}' contains repeated characters.")
    else:
        print(f"The string '{sample_string}' does not contain any repeated characters.")