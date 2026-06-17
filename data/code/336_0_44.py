import sys
def check_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_text = "Hello, World!"
    has_repeats = check_repeated_chars(sample_text)
    if has_repeats:
        print(f"The string '{sample_text}' contains repeated characters.")
        sys.exit(0)
    else:
        print(f"The string '{sample_text}' does not contain any repeated characters.")
        sys.exit(1)