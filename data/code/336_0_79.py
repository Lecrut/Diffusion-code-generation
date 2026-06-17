def check_repeated_chars(text):
    lower_text = text.lower()
    seen = set()
    for char in lower_text:
        if char in seen:
            return True, f"Repeated character found: '{char}'"
        seen.add(char)
    return False, "No repeated characters found."
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg",
        "AABBCCDD"
    ]
    for test_str in sample_strings:
        has_repeat, message = check_repeated_chars(test_str)
        print(f"'{test_str}': {message}")