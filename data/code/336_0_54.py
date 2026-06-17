def check_repeated_chars(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set:
            char_set.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "python", "abcdef"]
    found_repeats = []
    for s in sample_strings:
        if check_repeated_chars(s):
            found_repeats.append(s)
    print(f"Strings with repeated characters (case-insensitive): {found_repeats}")
    exit_code = 0 if len(found_repeats) > 0 else 1
    exit(exit_code)