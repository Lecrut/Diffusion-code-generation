import sys
def has_repeated_characters(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_text = "Hello World"
    result = has_repeated_characters(sample_text)
    print(f"Input string: {sample_text}")
    print(f"Contains repeated characters: {result}")
    if not result:
        sys.exit(1)