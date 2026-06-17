def check_repeated_chars(text):
    text_lower = text.lower()
    char_set = set()
    for ch in text_lower:
        if ch not in ' \t\n':                     
            if ch in char_set:
                return True
            char_set.add(ch)
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    for s in sample_strings:
        has_repeat = check_repeated_chars(s)
        status = "Contains repeated characters" if has_repeat else "No repeated characters found"
        print(f"'{s}': {status}")