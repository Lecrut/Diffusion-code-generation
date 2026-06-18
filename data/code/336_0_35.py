def check_repeated_chars(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if not char.isalpha():
            continue
        count = char_count.get(char, 0) + 1
        if count > 1:
            return True
        char_count[char] = count
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        if result:
            print(f"'{s}' contains repeated characters.")
        else:
            print(f"'{s}' has no repeated characters.")