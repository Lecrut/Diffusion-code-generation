def has_repeated_characters(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = has_repeated_characters(sample_string)
    if result:
        print(f"The string '{sample_string}' contains repeated characters.")
    else:
        print(f"The string '{sample_string}' does not contain any repeated characters.")