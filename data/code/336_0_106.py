import sys
def has_repeated_characters(s: str) -> bool:
    seen = set()
    for char in s.lower():
        if char == ' ':
            continue
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Python Script",
        "abcdefg"
    ]
    for test_str in sample_strings:
        if has_repeated_characters(test_str):
            print(f"'{test_str}' contains repeated characters.")
        else:
            print(f"'{test_str}' does not contain repeated characters.")
    sys.exit(0)