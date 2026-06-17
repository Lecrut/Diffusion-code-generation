def has_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char not in seen and char.isalpha():
            seen.add(char)
        elif char in seen:
            return True
    return False
if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = has_repeated_chars(sample_text)
    if result:
        print("The string contains repeated characters.")
    else:
        print("The string does not contain any repeated characters.")