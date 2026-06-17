def has_repeated_characters(text):
    seen = set()
    for char in text:
        if char.lower() in seen:
            return True
        seen.add(char.lower())
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello",
        "PythonScript",
        "abcdefg"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}': {'Contains repeated characters' if result else 'No repeated characters'}")