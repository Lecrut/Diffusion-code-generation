import sys
def has_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for ch in text_lower:
        if ch not in char_set:
            char_set.add(ch)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_text = "Hello World"
    result = has_repeated_chars(sample_text)
    print(f"Input string: '{sample_text}'")
    if result:
        print("Result: Repeated characters found.")
        sys.exit(0)
    else:
        print("Result: No repeated characters found.")
        sys.exit(1)