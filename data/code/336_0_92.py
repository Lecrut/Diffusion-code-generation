def check_repeated_chars(text):
    text = text.lower()
    seen = set()
    for char in text:
        if char not in seen and len(char) > 0:
            seen.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}': {'Contains repeated characters' if result else 'No repeated characters'}")