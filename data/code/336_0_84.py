import sys
def contains_repeated_chars(text: str) -> bool:
    chars = set()
    for char in text.lower():
        if char not in chars:
            chars.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdef",
        "Hello World!",
        "",
        "aA"
    ]
    for s in sample_strings:
        result = contains_repeated_chars(s)
        print(f"'{s}' -> {'Contains repeated characters' if result else 'No repeated characters'}")