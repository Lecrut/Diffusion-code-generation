def check_repeated_chars(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                      
            continue
        count = char_count.get(char, 0) + 1
        char_count[char] = count
        if count > 1:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}': {'Has repeated characters' if result else 'No repeated characters'}")