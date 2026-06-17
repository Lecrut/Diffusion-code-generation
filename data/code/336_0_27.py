def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    unique_chars = set(text_lower)
    return len(unique_chars) < len(text_lower)
if __name__ == '__main__':
    sample_text = "Hello, World!"
    has_repeat = check_repeated_chars(sample_text)
    if has_repeat:
        print(f"String '{sample_text}' contains repeated characters.")
    else:
        print(f"String '{sample_text}' does not contain any repeated characters.")