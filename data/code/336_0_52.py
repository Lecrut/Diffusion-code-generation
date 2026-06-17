def check_repeated_characters(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                                                                                                                                                                                       
            pass
        if char in char_count:
            return True
        else:
            char_count[char] = 1
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        print(f"'{s}': {'Repeated characters found' if result else 'No repeated characters'}")