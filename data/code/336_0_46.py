def has_repeated_chars(text):
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = has_repeated_chars(sample_text)
    print(f"String: {sample_text}")
    print(f"Contains repeated characters: {'Yes' if result else 'No'}")