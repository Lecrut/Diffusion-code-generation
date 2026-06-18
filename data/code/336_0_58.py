def check_repeated_characters(text: str) -> bool:
    normalized_text = text.lower()
    seen_chars = set()
    for char in normalized_text:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    for test_string in sample_strings:
        result = check_repeated_characters(test_string)
        print(f"'{test_string}': {'Repeated characters found' if result else 'No repeated characters'}")