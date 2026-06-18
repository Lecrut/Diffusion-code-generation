import sys
def has_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char not in seen:
            seen.add(char)
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