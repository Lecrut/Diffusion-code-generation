import sys
def has_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char not in seen:
            seen.add(char)
        else:
            return True
    return False
def main():
    sample_strings = [
        "Hello World",
        "Python3.12",
        "abcdefg"
    ]
    for s in sample_strings:
        result = has_repeated_chars(s)
        print(f"'{s}': {'Has repeated characters' if result else 'No repeated characters'}")
if __name__ == '__main__':
    main()