def contains_repeated_chars(text):
    text_lower = text.lower()
    seen = set()
    for char in text_lower:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "Python"]
    for s in sample_strings:
        result = contains_repeated_chars(s)
        output_status = "contains repeated characters" if result else "does not contain repeated characters"
        print(f"'{s}': {output_status}")