def has_repeated_characters(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "AaBbCc"]
    print("Testing string repetition detection:")
    for s in sample_strings:
        result = has_repeated_characters(s)
        status = "Contains repeated characters" if result else "No repeated characters"
        print(f"'{s}': {status}")