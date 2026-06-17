import sys
def check_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    return any(char in text_lower and char != '' for i, char in enumerate(text_lower))
if __name__ == '__main__':
    sample_text = "Hello World"
    if len(sample_text.split()) > 0:
        has_repeated_chars = check_repeated_characters(sample_text)
        print(f"Input string: {sample_text}")
        print(f"Has repeated characters: {'Yes' if has_repeated_chars else 'No'}")
if __name__ == '__main__':
    sys.exit(0)