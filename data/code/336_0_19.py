import sys
def check_repeated_chars(text: str) -> bool:
    return len(set(text.lower())) != len(text.lower())
if __name__ == '__main__':
    sample_text = "Hello World"
    has_repeat = check_repeated_chars(sample_text)
    if has_repeat:
        print(f"The string '{sample_text}' contains repeated characters.")
        sys.exit(0)
    else:
        print(f"The string '{sample_text}' does not contain any repeated characters.")
        sys.exit(1)