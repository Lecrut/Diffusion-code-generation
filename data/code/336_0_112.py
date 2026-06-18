def has_repeated_characters(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if not char.isalnum():                                                                                                            
            continue
        if char in char_set:
            return True
        char_set.add(char)
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "aabbcc"]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}': {'Contains repeated characters' if result else 'No repeated characters'}")