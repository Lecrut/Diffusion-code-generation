import sys
def check_repeated_chars(text: str) -> bool:
    if not text:
        return False
    lower_text = text.lower()
    seen_chars = set()
    for char in lower_text:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "Hello World!",
        "",
        "a"
    ]
    for test_str in sample_strings:
        result = check_repeated_chars(test_str)
        status = "Contains repeated characters" if result else "No repeated characters found"
        print(f"'{test_str}': {status}")