def check_repeated_characters(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if not (char.isalnum()):
            continue
        if char in char_set:
            return True
        char_set.add(char)
    return False
def main():
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        print(f"'{s}' contains repeated characters: {result}")
if __name__ == '__main__':
    main()